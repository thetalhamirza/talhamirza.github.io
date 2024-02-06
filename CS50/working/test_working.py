from working import convert
import pytest

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 10 AM") == "22:00 to 10:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    with pytest.raises(ValueError):
        convert("9 AM")
    with pytest.raises(ValueError):
        convert("13 AM to 25 PM")
    with pytest.raises(ValueError):
        convert("cat")
