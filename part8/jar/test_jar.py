from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    big_jar = Jar(24)
    assert big_jar.capacity == 24
    half_full_jar = Jar(12, 6)
    assert half_full_jar.capacity == 12
    assert half_full_jar.size == 6

# def test_initial_value():
#     obj_1 = MyClass(1, 2)
#     assert obj_1.public_attr_1 == 4
#     assert obj_1.public_attr_2 == 2

# def test_no_value():
#     with pytest.raises(Exception) as e_info:
#         obj = MyClass(1, 2)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(2)
    assert jar.size == 8
    with pytest.raises(ValueError):
        jar.deposit(20)