from twttr import shorten

def test_shorten_normal():
    assert shorten("Tomasz") == "Tmsz"
    assert shorten("Tomasz Piatek") == "Tmsz Ptk"
    assert shorten("RODODENDRON") == "RDDNDRN"

def test_shorten_numbers():
    assert shorten("Tom1988asz") == "Tm1988sz"
    assert shorten("1 2 3 4") == "1 2 3 4"

def test_shorten_punctuation():
    assert shorten("Therefore, I am sad") == "Thrfr,  m sd"