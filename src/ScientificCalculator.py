import math

class ScientificCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def power(self, base, exponent):
        return base ** exponent

    def square_root(self, x):
        if x < 0:
            raise ValueError("Square root of negative number is not allowed.")
        return math.sqrt(x)

    def logarithm(self, x, base=10):
        if x <= 0:
            raise ValueError("Logarithm of non-positive number is not allowed.")
        if base == 'e':
            return math.log(x)
        elif base <= 0:
            raise ValueError("Base must be positive.")
        return math.log(x, base)

    def sine(self, x):
        return math.sin(x)

    def cosine(self, x):
        return math.cos(x)

    def tangent(self, x):
        # Check for angles where tangent is undefined
        if math.isclose(x % math.pi, math.pi / 2, rel_tol=1e-9):
            raise ValueError("Tangent is undefined for this angle.")
        return math.tan(x)

    def degrees_to_radians(self, degrees):
        return math.radians(degrees)

    def radians_to_degrees(self, radians):
        return math.degrees(radians)