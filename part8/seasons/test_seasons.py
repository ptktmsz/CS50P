from seasons import validate_date, int_to_english
import pytest

def test_validate_date():
    assert validate_date("1988-08-28") == True
    assert validate_date("2873-01-01") == True
    assert validate_date("1982-13-05") == False
    assert validate_date("1988-08-32") == False
    assert validate_date("31-08-1988") == False
    assert validate_date("5th of September, 1982") == False


def test_int_to_english():
    assert int_to_english(5) == "Five minutes"
    assert int_to_english(567) == "Five hundred sixty-seven minutes"
    assert int_to_english(982345) == "Nine hundred eighty-two thousand, three hundred forty-five minutes"