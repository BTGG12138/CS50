"""
from datetime import date, datetime
# 直接构造
d = date(2000, 1, 1)                       # 2000-01-01
dt = datetime(2000, 1, 1, 9, 30, 0)        # 2000-01-01 09:30:00
# 从字符串解析(最常用,CS50 seasons 用这个）
d  = date.fromisoformat("2000-01-01")      # Python 3.7+，格式必须 YYYY-MM-DD
dt = datetime.fromisoformat("2000-01-01 09:30:00")
dt = datetime.fromisoformat("2000-01-01T09:30:00")   # ISO 标准
# 拿当前日期/时间
today = date.today()                       # 今天
now   = datetime.now()                     # 当前本地时间
utc   = datetime.utcnow()                  # 当前 UTC(不推荐，用 utcnow 的替代见下）

# 使用 inflect 转换数字
p = inflect.engine()
# andword="" 参数至关重要，它会去掉英文数字中的 "and" (例如: one hundred twenty)
words = p.number_to_words(total_minutes, andword="")
"""
"""
cd /home/btgg/Desktop/CS50/week8/seasons && python3 -m venv .venv && source .venv/bin/activate && python -m pip install num2words
cd /home/btgg/Desktop/CS50/week8/seasons && rm -rf venv && python3 -m venv venv && source venv/bin/activate && pip install --upgrade pip && pip install inflect
"""

from datetime import date
import inflect
def main():print(convert(input("Date of Birth: ")))
def convert(s):
    try:
        birth=date.fromisoformat(s)
        now=date(2000,1,1)
        return f"{inflect.engine().number_to_words((now-birth).days*24*60,andword="").capitalize()} minutes"
    except ValueError:return "Invalid date"
if __name__ == "__main__":main()