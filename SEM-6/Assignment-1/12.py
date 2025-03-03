class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        if not isinstance(other, Complex):
            return NotImplemented
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __repr__(self):
        return f"({self.real} + {self.imag}i)"
c1 = Complex(3, 4)
c2 = Complex(1, 2)
c3 = c1 + c2
print("Sum:", c3)


