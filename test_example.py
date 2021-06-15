
import pytest
from example import Complex

"""
You can't just define `z` and `w`:

z = Complex(2, 2)
w = Complex(1, 2)

... fixtures are needed!
"""

@pytest.fixture
def z():
    return Complex(4,3)

@pytest.fixture
def w():
    return Complex(1,2)

"""
Then write your tests. They're just a bunch
of functions and assertions.
"""

def test_repr(z, w):
    assert z.__repr__() == "4 + 3i"

def test_add(z, w):
    v = z + w
    assert str(v) == "5 + 5i"

@pytest.mark.skip  # Mark the test to be skipped by `pytest`
def test_mod(z):
    z.mod() == 5
