from twttr import shorten

def test_shorten():
    assert shorten("qweqwe") == "qwqw", "小写 e 没去掉"
    assert shorten("qwEqwE") == "qwqw", "大写 E 没去掉"
    assert shorten("") == "", "空字符串处理错误"
    #加个逗号输出报错信息
if __name__ == "__main__":
    test_shorten()
    print("通过通过")