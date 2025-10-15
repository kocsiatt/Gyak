import pytest
from Gyak import greet


@pytest.mark.parametrize(
    "inp, expected",
    [("", "Nem adtál meg nevet!"),
        ("Attila", "Szia, Attila!"),
        ("   Petra   ", "Szia, Petra!"),
        ("  Ágota", "Szia, Ágota!"),
     ("    ", "Nem adtál meg nevet!")]
)


def test_greet_variants(inp, expected):
    assert greet(inp) == expected