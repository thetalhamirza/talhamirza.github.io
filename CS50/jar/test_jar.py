from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(20)
    assert jar.capacity == 20

    with pytest.raises(ValueError):
        jar = Jar(-12)

def test_str():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == '🍪🍪🍪🍪🍪'


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(15)
    jar1 = Jar()
    assert jar1.deposit(5) == None
    

def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(2)
    jar1 = Jar()
    jar1.deposit(5)
    assert jar1.withdraw(2) == "Nom Nom"


