import pytest
from fuel import gauge, convert

def test_zeroDivision():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
    with pytest.raises(ZeroDivisionError):
        convert('0/0')
    with pytest.raises(ZeroDivisionError):
        convert('4/0')

def test_str():
    with pytest.raises(ValueError):
        convert('cat/dog')
    with pytest.raises(ValueError):
        convert('a/b')

def test_bigNumerator():
    with pytest.raises(ValueError):
        convert('3/2')
    with pytest.raises(ValueError):
        convert('4/1')


def test_convert():
    assert convert('1/4') == 25
    assert convert('1/2') == 50
    assert convert('3/4') == 75
    assert convert('4/4') == 100

def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(45) == '45%'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
