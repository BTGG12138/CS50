from working import convert
import pytest
def test_convert():
    assert convert("9 AM to 5 PM")=="09:00 to 17:00","应通过9 AM to 5 PM"
    assert convert("9:00 AM to 5:00 PM")=="09:00 to 17:00","应通过9:00 AM to 5:00 PM"
    assert convert("10 AM to 8:50 PM")=="10:00 to 20:50","应通过10 AM to 8:50 PM"
    assert convert("10:30 PM to 8 AM")=="22:30 to 08:00","应通过10:30 PM to 8 AM"
    with pytest.raises(ValueError):convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):convert("9 AM - 5 PM")
    with pytest.raises(ValueError):convert("09:00 AM - 17:00 PM")
    #反正要记住
if __name__=="__main__":
    test_convert()
    print("通过通过")