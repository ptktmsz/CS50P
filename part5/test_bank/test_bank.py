from bank import value

def test_value_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("hello man") == 0

def test_value_h():
    assert value("howdy") == 20
    assert value("h a i") == 20
    assert value("H0001") == 20

def test_value_else():
    assert value("cat") == 100
    assert value("choinka") == 100
    assert value("0123h") == 100