#!/usr/bin/env python3
"""
香港银行LOF (501025) 实时指标获取工具

通过东方财富免费API获取基金实时行情、净值、持仓等数据，无需API Key。

用法:
    python hk_bank_lof.py                # 获取全部指标
    python hk_bank_lof.py --watch        # 持续监控模式，每30秒刷新
    python hk_bank_lof.py --holdings     # 查看持仓明细
    python hk_bank_lof.py --history 15   # 查看最近15天历史净值
    python hk_bank_lof.py --code 501025  # 指定其他基金代码
"""

# ============================================================
# 【导入模块】
# Python 标准库，无需 pip install 安装任何东西
# ============================================================
import argparse      # 解析命令行参数，比如 --watch、--history 15
import json          # 解析 API 返回的 JSON 数据
import sys           # 系统相关（本次未直接使用，但保留备用）
import time          # time.sleep() 用于 --watch 模式的定时刷新
from datetime import datetime   # 处理日期时间，比如把时间戳转成 "2026-11-05"
from urllib.parse import quote  # 把中文做 URL 编码，比如 "香港银行" → "%E9%A6%99..."
from urllib.request import Request, urlopen  # 发起 HTTP 请求（替代 requests 库）
from urllib.error import URLError            # 捕获网络错误


# ============================================================
# 【常量与工具函数】
# ============================================================

# 默认查询的基金代码
# 501025 = 鹏华中证香港银行指数(LOF)A  ← 我们要查的
# 010365 = 鹏华中证香港银行指数(LOF)C  ← 同一只基金的C类份额
# A类有申购费无销售服务费；C类反过来，适合短线持有
DEFAULT_FUND_CODE = "501025"


def _market_prefix(code: str) -> str:
    """
    根据基金代码判断它在哪个交易所上市，返回东方财富API需要的"市场前缀"。

    东方财富的行情系统里，每只证券用一个 "市场.代码" 的格式标识：
      - 沪市（上海交易所）基金：代码以 50/51/52 开头 → 前缀 "1"
      - 深市（深圳交易所）基金：代码以 15/16 开头 → 前缀 "0"

    比如 501025 是沪市基金，所以 secid = "1.501025"
    """
    # startswith 可以接收元组，只要匹配其中任意一个前缀就返回 True
    return "1" if code.startswith(("50", "51", "52")) else "0"


def _fetch(url: str, charset: str = "utf-8", referer: str = "") -> str:
    """
    发起 HTTP GET 请求并返回响应文本。

    参数:
        url:     请求的完整 URL
        charset: 响应的字符编码（东方财富的接口都是 UTF-8）
        referer: HTTP Referer 头，有些接口会校验来源页面防止盗链

    为什么要自己写而不直接用 urlopen(url)?
        因为很多 API 会检查 User-Agent，如果不带浏览器 UA 就会返回 403 拒绝。
        Request 对象允许我们自定义请求头。
    """
    headers = {"User-Agent": "Mozilla/5.0"}  # 伪装成浏览器
    if referer:
        headers["Referer"] = referer
    req = Request(url, headers=headers)
    # urlopen 发起请求，timeout=15 表示最多等 15 秒
    with urlopen(req, timeout=15) as resp:
        # resp.read() 返回字节串(bytes)，.decode() 转成字符串(str)
        return resp.read().decode(charset)


def _div(val, factor):
    """
    东方财富的行情接口有个设计：数值是"原始值 × 精度因子"返回的。
    比如当前价 19.15，接口返回 1915，精度因子 100，需要 1915/100 = 19.15。

    这个函数做安全除法，处理各种边界情况（None、"-"、空字符串等）。
    """
    if val is None or val == "-" or val == "":
        return None
    try:
        return round(float(val) / factor, 4)  # round 保留4位小数
    except (ValueError, TypeError, ZeroDivisionError):
        return val  # 出错就原样返回


def _extract_js_array(raw: str, var_name: str):
    """
    从东方财富的 pingzhongdata.js 文件中提取某个 JS 数组变量。

    这个 JS 文件长这样：
        var Data_netWorthTrend = [{x:1793808000000, y:1.9344, ...}, ...];
        var Data_ACWorthTrend = [[1793808000000, 2.1173], ...];
        var Data_currentFundPosition = [{code:"00700", name:"腾讯", ...}, ...];

    思路：
        1. 找到 "变量名 = " 的位置
        2. 从那个位置开始，用括号深度计数找到完整的 [...] 闭包
        3. 把这段文本当 JSON 解析成 Python 列表

    为什么不直接用正则？
        因为数组可能嵌套很深，正则难以正确匹配，括号计数是最可靠的方式。
    """
    pattern = f"{var_name} = "
    if pattern not in raw:
        return None
    # 找到等号后面的起始位置
    start = raw.index(pattern) + len(pattern)
    # 用 depth 记录方括号的嵌套层级
    depth = 0
    for i in range(start, len(raw)):
        if raw[i] == "[":
            depth += 1           # 遇到 [ 说明进入更深层
        elif raw[i] == "]":
            depth -= 1           # 遇到 ] 说明退出一层
            if depth == 0:       # depth 回到0，说明最外层 ] 找到了
                # raw[start : i+1] 就是完整的数组文本
                return json.loads(raw[start : i + 1])
    return None  # 没找到完整闭包


# ============================================================
# 【1. 实时行情】
# 调用东方财富的 push2 行情接口，获取盘中实时价格
# ============================================================
def get_realtime_quote(code: str) -> dict:
    """
    获取实时行情数据。

    接口地址: https://push2.eastmoney.com/api/qt/stock/get
    关键参数:
        - secid: "市场前缀.基金代码"，如 "1.501025"
        - fields: 要获取哪些字段，用 f 编号指定
        - ut: 东方财富的通用令牌（公开值，非个人密钥）

    fields 编号对照（常用）:
        f43 = 最新价（需÷100）
        f44 = 最高价
        f45 = 最低价
        f46 = 开盘价
        f47 = 成交量（手）
        f48 = 成交额（元）
        f51 = 涨停价
        f52 = 跌停价
        f57 = 证券代码
        f58 = 证券名称
        f60 = 昨日收盘价
        f168 = 换手率（需÷100）
        f170 = 涨跌幅（需÷100）
        f171 = 振幅（需÷100）
    """
    # 拼接市场前缀，比如 501025 → "1.501025"
    secid = f"{_market_prefix(code)}.{code}"
    url = (
        f"https://push2.eastmoney.com/api/qt/stock/get"
        f"?secid={secid}"
        f"&fields=f43,f44,f45,f46,f47,f48,f50,f51,f52,f57,f58,f60,f170,f171,f168"
        f"&ut=fa5fd8884c8ac1fa104c3c09beec6a6e"  # 公开令牌，非密钥
    )
    try:
        raw = _fetch(url)                # 发起HTTP请求
        data = json.loads(raw)           # 把JSON字符串解析成Python字典
        # rc=0 表示接口调用成功
        if data.get("rc") != 0 or not data.get("data"):
            return {"提示": "未获取到行情数据（可能非交易时段）"}

        d = data["data"]  # 实际数据在 "data" 字段里
        # 用 _div 把原始值还原成真实数值
        return {
            "基金代码": d.get("f57"),
            "基金名称": d.get("f58"),
            "当前价": _div(d.get("f43"), 100),
            "涨跌幅(%)": _div(d.get("f170"), 100),
            "今开": _div(d.get("f46"), 100),
            "最高": _div(d.get("f44"), 100),
            "最低": _div(d.get("f45"), 100),
            "昨收": _div(d.get("f60"), 100),
            "涨停": _div(d.get("f51"), 100),
            "跌停": _div(d.get("f52"), 100),
            "成交量(手)": d.get("f47"),
            "成交额(元)": _div(d.get("f48"), 1),
            "换手率(%)": _div(d.get("f168"), 100),
            "振幅(%)": _div(d.get("f171"), 100),
        }
    except (URLError, json.JSONDecodeError, KeyError) as e:
        # 网络错误、JSON解析失败、字段缺失，都捕获并返回错误信息
        return {"error": f"行情接口异常: {e}"}


# ============================================================
# 【2. 基金净值】
# 从 pingzhongdata.js 提取净值数据
# ============================================================
def get_nav_info(code: str) -> dict:
    """
    获取最新的单位净值、累计净值、日增长率。

    接口地址: https://fund.eastmoney.com/pingzhongdata/{基金代码}.js
    这不是标准的 JSON API，而是一个 JS 文件，里面用 var 声明了很多变量：
        var fS_name = "鹏华中证香港银行指数(LOF)A";
        var fS_code = "501025";
        var Data_netWorthTrend = [{x:时间戳, y:单位净值, equityReturn:日增长率}, ...];
        var Data_ACWorthTrend = [[时间戳, 累计净值], ...];

    两个数组的数据结构不同：
        - netWorthTrend 的元素是字典 {x, y, equityReturn}
        - ACWorthTrend 的元素是列表 [时间戳, 值]
    这是东方财富的"历史设计"，只能分别处理。
    """
    url = f"https://fund.eastmoney.com/pingzhongdata/{code}.js"
    try:
        raw = _fetch(url)
        result = {}

        # ── 提取基金名称和代码（简单变量，格式: var fS_name = "xxx";）──
        for var, label in [("fS_name", "基金名称"), ("fS_code", "基金代码")]:
            pattern = f"{var} = "
            if pattern in raw:
                s = raw.index(pattern) + len(pattern)  # 跳过 "var xxx = "
                e = raw.index(";", s)                   # 找到行尾分号
                # json.loads 能解析带双引号的字符串，比如 '"hello"' → 'hello'
                result[label] = json.loads(raw[s:e])

        # ── 提取单位净值趋势（最新一条）──
        # Data_netWorthTrend 是一个长列表，每天一条记录，我们取最后一条
        nav_trend = _extract_js_array(raw, "Data_netWorthTrend")
        if nav_trend:
            latest = nav_trend[-1]          # 列表最后一个元素 = 最新数据
            ts = latest.get("x", 0)         # x 是毫秒级 Unix 时间戳
            # datetime.fromtimestamp() 把时间戳转成可读日期
            # 除以 1000 是因为 JS 用毫秒，Python 用秒
            result["净值日期"] = datetime.fromtimestamp(ts / 1000).strftime("%Y-%m-%d")
            result["单位净值"] = latest.get("y")
            result["日增长率(%)"] = latest.get("equityReturn")

        # ── 提取累计净值趋势（最新一条）──
        # Data_ACWorthTrend 格式: [[时间戳, 累计净值], ...]
        # 每个元素是列表而非字典，所以用 [1] 取第二个元素（累计净值）
        ac_trend = _extract_js_array(raw, "Data_ACWorthTrend")
        if ac_trend:
            result["累计净值"] = ac_trend[-1][1]  # [-1]最后一条, [1]取值

        return result
    except (URLError, json.JSONDecodeError, ValueError) as e:
        return {"error": f"净值接口异常: {e}"}


# ============================================================
# 【3. 持仓明细】
# 获取基金的前十大重仓股
# ============================================================
def get_holdings(code: str) -> list[dict]:
    """
    获取基金持仓数据。

    持仓数据来自基金季报（一季报/二季报/三季报/年报），
    所以会有延迟，通常在季度结束后1-2个月才公布。

    优先从 pingzhongdata.js 的 Data_currentFundPosition 提取；
    如果没有，尝试备用接口。
    """
    # ── 主接口：pingzhongdata.js ──
    url = f"https://fund.eastmoney.com/pingzhongdata/{code}.js"
    try:
        raw = _fetch(url)
        # Data_currentFundPosition 的每个元素是一个字典：
        #   {code: "00700", name: "腾讯控股", ratio: "9.83", amount: "12345", ...}
        arr = _extract_js_array(raw, "Data_currentFundPosition")
        if arr:
            holdings = []
            for item in arr[:10]:  # [:10] 取前10个，即前十大重仓
                holdings.append(
                    {
                        "股票代码": item.get("code"),
                        "股票名称": item.get("name"),
                        "持仓占比(%)": item.get("ratio"),
                        "持仓市值(万)": item.get("amount"),
                    }
                )
            return holdings
    except (URLError, json.JSONDecodeError, ValueError):
        pass  # 主接口失败，继续尝试备用接口

    # ── 备用接口（部分基金主接口没有持仓数据时尝试）──
    try:
        url2 = (
            f"https://fund.eastmoney.com/data/FundRankapi.aspx"
            f"?fundcode={code}&type=hold"
        )
        # 这个接口校验 Referer，不带的话可能返回空
        raw2 = _fetch(url2, referer="https://fund.eastmoney.com/")
        if raw2.strip():
            # 返回格式: var rankData = {hold: [[code, name, ...], ...]}
            start = raw2.index("=") + 2   # 跳过 "var rankData = "
            data = json.loads(raw2[start:].rstrip(";"))  # 去掉末尾分号
            items = data.get("hold", [])
            if items:
                return [
                    {
                        "股票代码": r[0],
                        "股票名称": r[1],
                        "持仓占比(%)": r[6],
                    }
                    for r in items[:10]  # 列表推导式，取前10条
                ]
    except Exception:
        # 备用接口也失败，不再重试
        pass

    # 两个接口都没有持仓数据，返回提示
    return [{"info": "持仓数据暂未公布（通常季报后更新）"}]


# ============================================================
# 【4. 历史净值】
# 获取最近 N 天的每日净值记录
# ============================================================
def get_nav_history(code: str, days: int = 10) -> list[dict]:
    """
    获取历史净值数据。

    接口地址: https://api.fund.eastmoney.com/f10/lsjz
    参数:
        - fundCode: 基金代码
        - pageIndex: 页码（从1开始）
        - pageSize: 每页条数（我们直接用它指定天数）
        - callback: 留空表示返回纯JSON而非JSONP

    返回格式:
        {
          "Data": {
            "LSJZList": [
              {"FSRQ": "2026-11-05", "DWJZ": "1.9344", "LJJZ": "2.1173", "JZZZL": "2.24"},
              ...
            ]
          }
        }
    字段说明:
        FSRQ  = 日期
        DWJZ  = 单位净值 (DW = 单位, JZ = 净值)
        LJJZ  = 累计净值 (LJ = 累计)
        JZZZL = 净值增长率 (ZZL = 增长率)
    """
    url = (
        f"https://api.fund.eastmoney.com/f10/lsjz"
        f"?fundCode={code}&pageIndex=1&pageSize={days}"
        f"&startDate=&endDate=&callback="
    )
    try:
        # 这个接口需要 Referer 头，否则返回 403
        raw = _fetch(url, referer="https://fund.eastmoney.com/")

        # 有些情况下接口会返回 JSONP 格式：
        #   jQuery1124088_1234567({"Data":...})
        # 我们需要去掉前面的回调函数名和包裹的括号
        if raw.lstrip().startswith(("jQuery", "callback", "var")):
            # raw.index("(") 找到第一个 ( ，raw.rindex(")") 找到最后一个 )
            # 取中间部分就是纯 JSON
            raw = raw[raw.index("(") + 1 : raw.rindex(")")]

        data = json.loads(raw)
        items = data.get("Data", {}).get("LSJZList", [])
        result = []
        for item in items:
            result.append(
                {
                    "日期": item.get("FSRQ"),
                    "单位净值": item.get("DWJZ"),
                    "累计净值": item.get("LJJZ"),
                    "日增长率(%)": item.get("JZZZL"),
                }
            )
        return result
    except (URLError, json.JSONDecodeError) as e:
        return [{"error": f"历史净值接口异常: {e}"}]


# ============================================================
# 【格式化输出函数】
# 把数据打印成整齐的表格，方便阅读
# ============================================================

def _print_table(data: dict, title: str = ""):
    """
    把字典打印成两列的键值表。

    示例输出:
        ────────────────────────────────
          💰 最新净值
        ────────────────────────────────
          基金名称      鹏华中证香港银行指数(LOF)A
          单位净值      1.9344
          累计净值      2.1173

    技巧: max_key 计算最长键名的长度，用 f-string 的 <N 左对齐填充，
    保证值列整齐对齐。
    """
    if title:
        print(f"\n{'─' * 52}")
        print(f"  {title}")
        print(f"{'─' * 52}")
    if "error" in data:
        print(f"  ⚠ {data['error']}")
        return
    if "info" in data:
        print(f"  ℹ {data['info']}")
        return
    if not data:
        print("  (无数据)")
        return
    # 找到最长的键名，用来对齐
    max_key = max(len(str(k)) for k in data.keys())
    for k, v in data.items():
        # 成交额数字很大，加千分位逗号方便阅读
        if "成交额" in str(k) and isinstance(v, (int, float)) and v > 10000:
            v = f"{v:,.0f}"  # :, 加千分位逗号
        # f"{str(k):<{max_key+2}}" 表示左对齐，宽度为 max_key+2
        print(f"  {str(k):<{max_key + 2}} {v if v is not None else '-'}")


def _print_list_table(rows: list[dict], title: str = ""):
    """
    把列表[字典]打印成多列表格。

    示例输出:
        ────────────────────────────────────────
          📊 最近 7 天净值走势
        ────────────────────────────────────────
          日期            单位净值      累计净值      日增长率(%)
          ────────────────────────────────────────
          2026-11-05    1.9344    2.1173    2.24
          2026-11-04    1.8921    2.0750    1.43

    技巧: 先遍历所有行计算每列最大宽度，再统一格式化输出。
    """
    if title:
        print(f"\n{'─' * 62}")
        print(f"  {title}")
        print(f"{'─' * 62}")
    if not rows:
        print("  (无数据)")
        return
    first = rows[0]
    # 第一行如果是错误/提示信息，直接显示
    if "error" in first or "info" in first:
        msg = first.get("error") or first.get("info")
        icon = "⚠" if "error" in first else "ℹ"
        print(f"  {icon} {msg}")
        return

    # 取所有列名（字典的键）
    keys = list(first.keys())

    # 计算每列宽度 = max(列名长度, 该列所有值的最大长度) + 2（留间距）
    # 字典推导式 + 生成器表达式，一行搞定
    col_w = {
        k: max(len(k), max(len(str(r.get(k, ""))) for r in rows)) + 2
        for k in keys
    }

    # 打印表头
    header = "  ".join(f"{k:<{col_w[k]}}" for k in keys)
    print(f"  {header}")
    print(f"  {'─' * len(header)}")

    # 打印每一行数据
    for row in rows:
        line = "  ".join(f"{str(row.get(k, '-')):<{col_w[k]}}" for k in keys)
        print(f"  {line}")


# ============================================================
# 【主函数】
# 解析命令行参数 → 调用各API → 格式化输出 → (可选)循环刷新
# ============================================================
def main():
    # ── argparse: 命令行参数解析 ──
    # 用法示例: python hk_bank_lof.py --watch --history 10
    parser = argparse.ArgumentParser(
        description="香港银行LOF 实时指标查询",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""  # epilog 是帮助信息底部的额外文字
示例:
  python hk_bank_lof.py                  # 查看实时行情 + 最新净值
  python hk_bank_lof.py --watch          # 每30秒刷新一次
  python hk_bank_lof.py --holdings       # 查看持仓明细
  python hk_bank_lof.py --history 15     # 最近15天净值走势
  python hk_bank_lof.py --code 010365    # 查看 C 类份额
""",
    )
    # 添加 --code 参数，可选，默认 501025
    parser.add_argument(
        "--code",
        default=DEFAULT_FUND_CODE,
        help=f"基金代码 (默认: {DEFAULT_FUND_CODE})",
    )
    # 添加 --watch 开关，不带值，出现即为 True
    parser.add_argument(
        "--watch", action="store_true", help="持续监控模式，每30秒刷新"
    )
    # 添加 --holdings 开关
    parser.add_argument(
        "--holdings", action="store_true", help="查看持仓明细"
    )
    # 添加 --history 参数，需要跟一个整数，如 --history 10
    # default=0 表示不传这个参数时不查历史
    parser.add_argument(
        "--history",
        type=int,
        default=0,
        help="查看最近N天历史净值，如 --history 10",
    )
    # parse_args() 把命令行参数解析成对象属性
    args = parser.parse_args()
    code = args.code

    # ── 主循环（--watch 模式下会一直循环，普通模式只执行一次）──
    while True:
        # 打印标题栏
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n{'━' * 62}")
        print(f"  香港银行LOF ({code})  ·  {now}")
        print(f"{'━' * 62}")

        # 获取并显示实时行情
        quote = get_realtime_quote(code)
        _print_table(quote, "📈 实时行情 (盘中)")

        # 获取并显示最新净值
        nav = get_nav_info(code)
        _print_table(nav, "💰 最新净值")

        # 如果传了 --holdings，获取并显示持仓
        if args.holdings:
            holdings = get_holdings(code)
            _print_list_table(holdings, "🏦 前十大重仓股")

        # 如果传了 --history N，获取并显示最近N天历史净值
        if args.history > 0:
            history = get_nav_history(code, args.history)
            _print_list_table(history, f"📊 最近 {args.history} 天净值走势")

        print()  # 空行分隔

        # 非 watch 模式，查一次就退出
        if not args.watch:
            break

        # watch 模式：等30秒后重新查询
        print("  ⏳ 30秒后刷新... (Ctrl+C 退出)")
        try:
            time.sleep(30)
        except KeyboardInterrupt:
            # 用户按 Ctrl+C 中断等待，退出循环
            print("\n  已退出监控模式。")
            break


# ============================================================
# 【程序入口】
# 当直接运行 python hk_bank_lof.py 时，__name__ == "__main__"
# 这时调用 main()；如果被其他脚本 import，则不会自动执行
# ============================================================
if __name__ == "__main__":
    main()