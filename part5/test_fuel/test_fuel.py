from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("99/100") == 99
    assert convert("1/3") == 33

def test_convert_errors():
    with pytest.raises(ValueError):
        convert("6/5")
    with pytest.raises(ZeroDivisionError):
        convert("6/0")


def test_gauge():
    assert gauge(int("50")) == "50%"
    assert gauge(int("12")) == "12%"
    assert gauge(int("88")) == "88%"
    assert gauge(int("1")) == "E"
    assert gauge(int("99")) == "F"