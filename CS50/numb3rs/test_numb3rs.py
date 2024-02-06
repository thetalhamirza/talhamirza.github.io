from numb3rs import validate


def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.105.252") == True
    assert validate("cat") == False
    assert validate("1.1.1.1.1") == False
    assert validate("8.8.8") == False
    assert validate("0") == False
    assert validate("256.0.0.1") == False
    assert validate("0.512.512.512") == False
