from project import check, check4d, wikiurl

def test_check():
    assert check("Didier Drogba", "Didier Drogba") == True
    assert check("didier drogba", "Didier Drogba") == True
    assert check("Drogba", "Didier Drogba") == False
    assert check("Sead Kolasinac", "Sead Kolašinac") == True

def test_check4d():
    assert check4d("1998") == True
    assert check4d("1998-2012") == True
    assert check4d("1998-") == True
    assert check4d("199") == False
    assert check4d("Years") == False

def test_wikiurl():
    assert wikiurl("Sead Kolašinac") == "https://en.wikipedia.org/wiki/Sead_Kolašinac"
    assert wikiurl("Didier Drogba") == "https://en.wikipedia.org/wiki/Didier_Drogba"
    assert wikiurl("Gerson") == "https://en.wikipedia.org/wiki/Gerson_(footballer,_born_1997)"