from working import convert
import pytest

def test_am():
    assert convert("9:00 AM to 11:00 AM") == "09:00 to 11:00"
    assert convert("5:46 AM to 7:13 AM") == "05:46 to 07:13"
    assert convert("6 AM to 7 AM") == "06:00 to 07:00"
    assert convert("12:00 AM to 1:00 AM") == "00:00 to 01:00"

def test_pm():
    assert convert("9:00 PM to 11:00 PM") == "21:00 to 23:00"
    assert convert("5:46 PM to 7:13 AM") == "17:46 to 07:13"
    assert convert("6 PM to 7 PM") == "18:00 to 19:00"
    assert convert("12:00 PM to 1:00 PM") == "12:00 to 13:00"

def test_mix():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("11:32 PM to 7:04 AM") == "23:32 to 07:04"

def test_invalid():
    with pytest.raises(ValueError):
        convert("15 AM to 6 PM")
    with pytest.raises(ValueError):
        convert("5 AM 6 PM")
    with pytest.raises(ValueError):
        convert("6 AM to 17 PM")
    with pytest.raises(ValueError):
        convert("10:78 AM to 2:22 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM 17:00 PM")
    with pytest.raises(ValueError):
        convert("9 to 5")