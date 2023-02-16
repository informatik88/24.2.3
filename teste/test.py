import pytest

from app.calc import Calculator

class TestClass:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 3, 4) == 7

    def test_subtraction(self):
        assert self.calc.subtraction(self, 7, 3) == 4

    def test_multiply(self):
        assert self.calc.multiply(self, 4, 6) == 24

    def test_division(self):
        assert self.calc.division(self, 9, 3) == 3

    def teardown(self):
        print('Выполнение метода Teardown')
