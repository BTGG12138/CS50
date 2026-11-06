from bank import value
def test_value():
    assert value("hello")==int(0),"hello检测失败"
    assert value("hhhhh")==int(20),"h检测失败"
    assert value("11111")==int(100),"随机输入检测失败"
    assert value("")==int(100),"空输入检测失败"
if __name__=="__main__":
    test_value()
    print("通过通过 ")