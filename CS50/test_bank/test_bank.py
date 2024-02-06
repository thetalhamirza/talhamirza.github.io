from bank import value

def test_hello():
    assert value("hello") == 0

def test_hstart():
    assert value("hi") == 20
    assert value("hey there!") == 20
    assert value("hong kong") == 20

def test_nothstart():
    assert value("welcome") == 100
    assert value("well hello there") == 100
    assert value("oh hi there!") == 100

def test_leadingspaces():
    assert value("    hello there") == 0
    assert value("    hi there") == 20
    assert value("    welcome") == 100

def test_case():
    assert value("HELLO THERE!") == 0
    assert value("HEY THERE") == 20
    assert value("WELCOME") == 100
    assert value("HeLlO tHeRe") == 0
