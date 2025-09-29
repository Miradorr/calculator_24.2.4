import pytest
from app.calc import Calculator

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()

    def test_add(self):
        assert self.calc.add(2, 3) == 5

    def test_subtract(self):
        assert self.calc.subtract(7, 4) == 3

    def test_multiply(self):
        assert self.calc.multiply(6, 5) == 30

    def test_divide(self):
        assert self.calc.divide(10, 2) == 5

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(5, 0)
