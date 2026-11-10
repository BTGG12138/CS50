from jar import Jar
import pytest
def test_init():
    jar = Jar()
    assert jar._capacity == 12
    assert jar._size == 0
    jar = Jar(5)
    assert jar._capacity == 5
    assert jar._size == 0
    with pytest.raises(ValueError):Jar(-1)
def test_str():
    jar=Jar(3)
    jar.deposit(2)
    assert str(jar)=="🍪🍪"
def test_deposit():
    jar=Jar(5)
    jar.deposit(2)
    jar.deposit(2)
    assert jar._size==4
    with pytest.raises(ValueError):jar.deposit(2)
def test_withdraw():
    jar=Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar._size==2
    with pytest.raises(ValueError):jar.withdraw(3)
if __name__=="__main__":
    test_init()
    test_str()
    test_deposit()
    test_withdraw()
    print("通过通过")