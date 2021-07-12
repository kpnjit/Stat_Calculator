import unittest

from Calculator.Calculator import Calculator
from CSVReader.CsvReader import CsvReader

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator.Calculator.Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator.Calculator.Calculator)

    def test_add_method_calculator(self):
        test_data = CsvReader("Tests/Data/Addition.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_sub_method_calculator(self):
        test_data = CsvReader("Tests/Data/Subtraction.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.sub(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiply_method_calculator(self):
        test_data = CsvReader("Tests/Data/Multiplication.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_divide_method_calculator(self):
        test_data = CsvReader("Tests/Data/Division.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square_method_calculator(self):
        test_data = CsvReader("Tests/Data/Square.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.squares(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_sqrt_method_calculator(self):
        test_data = CsvReader("Tests/Data/Square Root.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.square_root(row['Value 1']), round(float(row['Result']), 7))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 7))


if __name__ == '__main__':
    unittest.main()