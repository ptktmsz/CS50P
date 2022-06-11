from plates import is_valid

def test_nchar():
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False
    assert is_valid("A") == False


def test_start2l():
    assert is_valid("aB5647") == True
    assert is_valid("abcdef") == True
    assert is_valid("T0MASZ") == False
    assert is_valid("99masz") == False
    assert is_valid("123456") == False


def test_nend():
    assert is_valid("ab3647") == True
    assert is_valid("abcdef") == True
    assert is_valid("T0123Z") == False
    assert is_valid("To22sz") == False
    assert is_valid("aaa0AA") == False


def test_nstartnot0():
    assert is_valid("KKK345") == True
    assert is_valid("ABCDE3") == True
    assert is_valid("abcde0") == False
    assert is_valid("pp0345") == False
    assert is_valid("aa0000") == False


def test_nopunct():
    assert is_valid("ABC123") == True
    assert is_valid("AB 123") == False
    assert is_valid("A!bcde") == False
    assert is_valid("ooo(a)") == False