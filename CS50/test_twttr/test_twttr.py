from twttr import shorten

def test_onlyvowel():
    assert shorten("aeiou") == ''

def test_onlyconsonant():
    assert shorten("sqrt") == 'sqrt'

def test_vowelpresence():
    assert shorten("Hello World!") == 'Hll Wrld!'

def test_case():
    assert shorten("A Quick Brown Fox") == ' Qck Brwn Fx'

def test_number():
    assert shorten("123456789") == '123456789'
