from plates import is_valid

def test_twoletter_start():
    assert is_valid("AA") == True
    assert is_valid("BB") == True
    assert is_valid("CC") == True
    assert is_valid("A1") == False
    assert is_valid("2B") == False
    assert is_valid("33") == False

def test_strlength():
    assert is_valid("AA") == True
    assert is_valid("BBB") == True
    assert is_valid("EEEEEE") == True
    assert is_valid("F") == False
    assert is_valid("GGGGGGG") == False

def test_numberatend():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("BB1234") == True

def test_firstint0():
    assert is_valid("BB0123") == False
    assert is_valid("AB0000") == False
    assert is_valid("AC1000") == True

def test_punctuation():
    assert is_valid("BB1.23") == False
    assert is_valid("BB.,12") == False

