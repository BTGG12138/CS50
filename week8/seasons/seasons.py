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
"""
from datetime import date
def main():

if __name__ == "__main__":
    main()