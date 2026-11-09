from um import count
def test_count():
    assert count("um")==int(1),"um输出错误"
    assert count("um?")==int(1),"um?输出错误"
    assert count("Um, thanks for the album.")==int(1),"Um, thanks for the album.输出错误"
    assert count("Um, thanks, um...")==int(2),"Um, thanks, um...输出错误"
if __name__=="__main__":
    test_count()
    print("通过通过")