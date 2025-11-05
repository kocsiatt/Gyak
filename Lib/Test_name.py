import pytest
from Gyak import greet
from Gyak import check_password_strength





@pytest.mark.parametrize(
    "inp, expected",
    [("abc", "Gyenge jelszó: túl rövid."),
        ("ABCDEFGHIJKL", "Gyenge jelszó: nincs benne kisbetű."),
        ("abcdefghijkl", "Gyenge jelszó: nincs nagybetű."),
        ("Abcdefghijkl", "Gyenge jelszó: nincs benne szám.")]
)

def test_check_password_strength(inp, expected):
    assert check_password_strength(inp) == expected



"""@pytest.mark.parametrize(
    "inp, expected",
     [("", "Nem adtál meg nevet!"),
        ("Attila", "Szia, Attila!"),
        ("   Petra   ", "Szia, Petra!"),
        ("  Ágota", "Szia, Ágota!"),
        ("    ", "Nem adtál meg nevet!")]
)"""


"""def test_greet_variants(inp, expected):
    assert greet(inp) == expected"""