from fuel import convert
from fuel import gauge
import pytest
def convert_test():
    assert convert("2/3")==int(67),"应正常输出'1/3'"
    assert convert("2/2")==int(100),"应正常输出'2/2'"
    assert convert("0/2")==int(0),"应正常输出'0/2'"
    with pytest.raises(ValueError):convert("")
    #预期函数返回错误用这个
    with pytest.raises(ValueError):convert("3/2")
    with pytest.raises(ValueError):convert("3/0")
    with pytest.raises(ZeroDivisionError):convert("0/0")

def gauge_test():
    assert gauge(int(67))=="67%"
    assert gauge(int(100))=="F"
    assert gauge(int(0))=="E"

if __name__=="__main__":
    convert_test()
    gauge_test()
    print("通过通过 ")