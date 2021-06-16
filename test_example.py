
import pytest
from example import Complex

# Tests are just a bunch of functions and assertions.
def test_repr():
    z = Complex(4, 3)
    assert z.__repr__() == "4 + 3i"

def test_add():
    z = Complex(4, 3)
    w = Complex(1, 2)
    v = z + w
    assert str(v) == "5 + 5i"

# Homework! Implement this test.
@pytest.mark.skip 
def test_mod():
    pass
