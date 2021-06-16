from math import sqrt

class Complex:
    """ 
    Example class to play around with complex numbers and tests. 
    """

    def __init__(self, a: float, b: float):
        """
        A complex number has a real part (a) and imaginary part (b).
        """
        self.a = a
        self.b = b

    def __repr__(self):
        """ 
        The `__repr__` method defines how objects from this class are displayed.
        """
        return f"{self.a} + {self.b}i"

    def __add__(self, other):
        """ 
        The `__repr__` `add` method defines what the `+` operator does.
        """
        return Complex(self.a + other.a, self.b + other.b)

    def mod(self):
        """
        This method returns the modulus of the complex number.
        """
        raise sqrt(self.a**2 + self.b**2)
