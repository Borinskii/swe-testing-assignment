import pytest
from calculator import Calculator


class TestAddition:
    def setup_method(self):
        self.calc = Calculator()

    def test_add_two_positive_numbers(self):
        assert self.calc.add(5, 3) == 8

    def test_add_negative_numbers(self):
        # edge case: both operands negative
        assert self.calc.add(-4, -6) == -10


class TestSubtraction:
    def setup_method(self):
        self.calc = Calculator()

    def test_subtract_two_positive_numbers(self):
        assert self.calc.subtract(10, 4) == 6

    def test_subtract_resulting_in_negative(self):
        # edge case: result is negative
        assert self.calc.subtract(3, 9) == -6


class TestMultiplication:
    def setup_method(self):
        self.calc = Calculator()

    def test_multiply_two_positive_numbers(self):
        assert self.calc.multiply(6, 7) == 42

    def test_multiply_large_numbers(self):
        # edge case: very large numbers
        assert self.calc.multiply(1_000_000, 1_000_000) == 1_000_000_000_000


class TestDivision:
    def setup_method(self):
        self.calc = Calculator()

    def test_divide_two_positive_numbers(self):
        assert self.calc.divide(10, 2) == 5.0

    def test_divide_resulting_in_decimal(self):
        # edge case: decimal result
        assert self.calc.divide(1, 3) == pytest.approx(0.3333, rel=1e-3)

    def test_divide_by_zero_raises_value_error(self):
        # edge case: division by zero must raise ValueError
        with pytest.raises(ValueError, match="Division by zero is not allowed."):
            self.calc.divide(5, 0)


class TestNegate:
    def setup_method(self):
        self.calc = Calculator()

    def test_negate_positive_number(self):
        assert self.calc.negate(5) == -5

    def test_negate_negative_number(self):
        assert self.calc.negate(-5) == 5


class TestClear:
    def setup_method(self):
        self.calc = Calculator()

    def test_clear_resets_result_to_zero(self):
        self.calc.result = 99
        self.calc.clear()
        assert self.calc.result == 0