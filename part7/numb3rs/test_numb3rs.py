from numb3rs import validate

def test_range():
    assert validate("0.1.2.3") == True
    assert validate("255.255.255.255") == True
    assert validate("120.120.2.260") == False

def test_syntax():
    assert validate("0.0.0.0") == True
    assert validate("0.0.0") == False
    assert validate("0.0.0.0.0") == False
    assert validate("0,0,0,0") == False