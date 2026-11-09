from seasons import convert
def test_convert():
    assert convert("January 1, 1999")=="Invalid date","January 1, 1999"
    assert convert("1999-01-01")=="Five hundred twenty-five thousand, six hundred minutes","1999-01-01"
    assert convert("1999-12-31")=="One thousand, four hundred forty minutes","1999-12-31"
    assert convert("1970-01-01")=="Fifteen million, seven hundred seventy-eight thousand eighty minutes","1970-01-01"
if __name__=="__main__":
    test_convert()
    print("通过通过")
#find /home/btgg/Desktop/CS50/ -depth -type d \( -name "venv" -o -name "cache" -o -name ".cache" -o -name "__pycache__" \) -exec rm -rf {} +