import unittest
import math

# Assuming ScientificCalculator class is available in the scope or imported from a module
# For the purpose of this test, we'll redefine it here to ensure it's available.
# In a real scenario, you would import it: from your_module import ScientificCalculator

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
        # Using math.isclose for floating point comparison
        # Tangent is undefined at pi/2 + n*pi
        # We need to check if x is close to (pi/2) or (3*pi/2) etc.
        # x % math.pi will give a value between 0 and pi.
        # If x is pi/2 + n*pi, then x % math.pi will be pi/2.
        if math.isclose(x % math.pi, math.pi / 2, rel_tol=1e-9, abs_tol=1e-9):
            raise ValueError("Tangent is undefined for this angle.")
        return math.tan(x)

    def degrees_to_radians(self, degrees):
        return math.radians(degrees)

    def radians_to_degrees(self, radians):
        return math.degrees(radians)


class TestScientificCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = ScientificCalculator()

    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(0.5, 0.25), 0.75)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-2, 3), 1)
        self.assertEqual(self.calc.add(2, -3), -1)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0.75, 0.25), 0.5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5, -3), 8)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0.5, 0.5), 0.25)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(2, -3), -6)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(1, 2), 0.5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-6, -3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(6, -3), -2)

    def test_divide_by_one(self):
        self.assertEqual(self.calc.divide(5, 1), 5)

    def test_divide_zero_by_number(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_divide_by_zero_error(self):
        with self.assertRaisesRegex(ValueError, "Division by zero is not allowed."):
            self.calc.divide(5, 0)
        with self.assertRaisesRegex(ValueError, "Division by zero is not allowed."):
            self.calc.divide(0, 0)

    def test_power_positive_exponents(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(10, 1), 10)

    def test_power_negative_exponents(self):
        self.assertEqual(self.calc.power(2, -1), 0.5)
        self.assertEqual(self.calc.power(2, -2), 0.25)

    def test_power_fractional_exponents(self):
        self.assertAlmostEqual(self.calc.power(4, 0.5), 2.0)
        self.assertAlmostEqual(self.calc.power(8, 1/3), 2.0)

    def test_power_base_zero(self):
        self.assertEqual(self.calc.power(0, 5), 0)
        self.assertEqual(self.calc.power(0, 0), 1) # 0^0 is typically 1 in math/programming contexts

    def test_square_root_positive_numbers(self):
        self.assertEqual(self.calc.square_root(4), 2)
        self.assertAlmostEqual(self.calc.square_root(2), 1.4142135623730951)
        self.assertEqual(self.calc.square_root(0), 0)

    def test_square_root_negative_number_error(self):
        with self.assertRaisesRegex(ValueError, "Square root of negative number is not allowed."):
            self.calc.square_root(-1)
        with self.assertRaisesRegex(ValueError, "Square root of negative number is not allowed."):
            self.calc.square_root(-0.0001)

    def test_logarithm_positive_numbers_default_base(self):
        self.assertAlmostEqual(self.calc.logarithm(100), 2)
        self.assertAlmostEqual(self.calc.logarithm(1), 0)

    def test_logarithm_positive_numbers_custom_base(self):
        self.assertAlmostEqual(self.calc.logarithm(8, 2), 3)
        self.assertAlmostEqual(self.calc.logarithm(16, 4), 2)

    def test_logarithm_positive_numbers_natural_log(self):
        self.assertAlmostEqual(self.calc.logarithm(math.e, 'e'), 1)
        self.assertAlmostEqual(self.calc.logarithm(math.e**2, 'e'), 2)

    def test_logarithm_non_positive_x_error(self):
        with self.assertRaisesRegex(ValueError, "Logarithm of non-positive number is not allowed."):
            self.calc.logarithm(0)
        with self.assertRaisesRegex(ValueError, "Logarithm of non-positive number is not allowed."):
            self.calc.logarithm(-1)

    def test_logarithm_non_positive_base_error(self):
        with self.assertRaisesRegex(ValueError, "Base must be positive."):
            self.calc.logarithm(10, 0)
        with self.assertRaisesRegex(ValueError, "Base must be positive."):
            self.calc.logarithm(10, -2)

    def test_sine_common_angles(self):
        self.assertAlmostEqual(self.calc.sine(0), 0)
        self.assertAlmostEqual(self.calc.sine(math.pi / 2), 1)
        self.assertAlmostEqual(self.calc.sine(math.pi), 0)
        self.assertAlmostEqual(self.calc.sine(3 * math.pi / 2), -1)
        self.assertAlmostEqual(self.calc.sine(2 * math.pi), 0)

    def test_sine_negative_angles(self):
        self.assertAlmostEqual(self.calc.sine(-math.pi / 2), -1)
        self.assertAlmostEqual(self.calc.sine(-math.pi), 0)

    def test_cosine_common_angles(self):
        self.assertAlmostEqual(self.calc.cosine(0), 1)
        self.assertAlmostEqual(self.calc.cosine(math.pi / 2), 0)
        self.assertAlmostEqual(self.calc.cosine(math.pi), -1)
        self.assertAlmostEqual(self.calc.cosine(3 * math.pi / 2), 0)
        self.assertAlmostEqual(self.calc.cosine(2 * math.pi), 1)

    def test_cosine_negative_angles(self):
        self.assertAlmostEqual(self.calc.cosine(-math.pi / 2), 0)
        self.assertAlmostEqual(self.calc.cosine(-math.pi), -1)

    def test_tangent_common_angles(self):
        self.assertAlmostEqual(self.calc.tangent(0), 0)
        self.assertAlmostEqual(self.calc.tangent(math.pi / 4), 1)
        self.assertAlmostEqual(self.calc.tangent(-math.pi / 4), -1)
        self.assertAlmostEqual(self.calc.tangent(math.pi), 0)

    def test_tangent_undefined_angles_error(self):
        with self.assertRaisesRegex(ValueError, "Tangent is undefined for this angle."):
            self.calc.tangent(math.pi / 2)
        with self.assertRaisesRegex(ValueError, "Tangent is undefined for this angle."):
            self.calc.tangent(3 * math.pi / 2)
        with self.assertRaisesRegex(ValueError, "Tangent is undefined for this angle."):
            self.calc.tangent(-math.pi / 2)
        with self.assertRaisesRegex(ValueError, "Tangent is undefined for this angle."):
            self.calc.tangent(math.pi / 2 + 2 * math.pi) # Test with multiple rotations

    def test_degrees_to_radians_common_values(self):
        self.assertAlmostEqual(self.calc.degrees_to_radians(0), 0)
        self.assertAlmostEqual(self.calc.degrees_to_radians(90), math.pi / 2)
        self.assertAlmostEqual(self.calc.degrees_to_radians(180), math.pi)
        self.assertAlmostEqual(self.calc.degrees_to_radians(360), 2 * math.pi)
        self.assertAlmostEqual(self.calc.degrees_to_radians(-90), -math.pi / 2)

    def test_radians_to_degrees_common_values(self):
        self.assertAlmostEqual(self.calc.radians_to_degrees(0), 0)
        self.assertAlmostEqual(self.calc.radians_to_degrees(math.pi / 2), 90)
        self.assertAlmostEqual(self.calc.radians_to_degrees(math.pi), 180)
        self.assertAlmostEqual(self.calc.radians_to_degrees(2 * math.pi), 360)
        self.assertAlmostEqual(self.calc.radians_to_degrees(-math.pi / 2), -90)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)