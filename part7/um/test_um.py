from um import count
import pytest

def test_count():
    assert count("um") == 1
    assert count("um um") == 2
    assert count("u m") == 0

def test_case():
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("UM um UM um Um uM") == 6

def test_solitaryums():
    assert count("umami") == 0
    assert count("Um, thanks for the album.") == 1
    assert count("Um, umm, ummm") == 1