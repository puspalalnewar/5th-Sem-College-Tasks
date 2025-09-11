class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def sub(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def display(self):
        print("{" + str(self.real) + " + " + str(self.imag) + "i}")

# Example usage
c1 = Complex(2, 3)
c2 = Complex(1, 4)

print("First Complex Number: ", end="")
c1.display()

print("Second Complex Number: ", end="")
c2.display()

print("Addition: ", end="")
c1.add(c2).display()

print("Subtraction: ", end="")
c1.sub(c2).display()
