from numb3rs import validate
def test_validate():
    assert validate("0.0.0.0")==True,"应通过 0.0.0.0"
    assert validate("255.255.255.255")==True,"应通过 255.255.255.255"
    assert validate("")==False,"应不通过空输入"
    assert validate("-1,-1,-1,-1")==False,"应不通过 -1,-1,-1,-1"
    assert validate("256,256,256,256")==False,"应不通过 256,256,256,256"
    assert validate("001,002,100,200")==False,"应不通过 001,002,100,200"
    assert validate("a,b,c,d")==False,"应不通过 a,b,c,d"
if __name__=="__main__":
    test_validate()
    print("通过通过")