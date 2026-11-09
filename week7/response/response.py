"""
cd /home/btgg/Desktop/CS50/week7/response && \
python3 -m venv venv && \
source venv/bin/activate && \
python -m pip install --upgrade pip && \
python -m pip install validator-collection==1.5.0 && \
python -c "import validator_collection as vc; print('OK', vc.__version__)"
"""

"""
# 仅做判断，不关心具体错误原因
print(checkers.is_email('test@domain.dev')) # 输出: True
print(checkers.is_email('not-an-email'))    # 输出: False
# 对 None 也能安全处理，不会崩溃
print(checkers.is_email(None))              # 输出: False
"""

from validator_collection import checkers
if checkers.is_email(input("输入输入 ")):print("Valid")
else:print("Invalid")