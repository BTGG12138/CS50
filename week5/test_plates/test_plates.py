from plates import is_valid
def is_valid_test():
    assert is_valid(" ，。/-=")==False,"应只有字母和数字"
    assert is_valid("1234567")==False,"长度应在2-6之间"
    assert is_valid("")==False,"空输入错误"
    assert is_valid("as12as")==False,"末尾应不存在字母"
    assert is_valid("as0001")==False,"第一个数字应不存在0"
    assert is_valid("1a1211")==False,"第一位应不存在字母"
    assert is_valid("a11211")==False,"第二位应不存在字母"
if __name__=="__main__":
    is_valid_test()
    print("通过通过 ")