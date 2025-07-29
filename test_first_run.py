
import unittest
from first_run import add_operation, subtract_operation

class TestOperations(unittest.TestCase):

    def test_add_operation_positive_numbers(self):
        self.assertEqual(add_operation(2, 3), 5)

    def test_add_operation_negative_numbers(self):
        self.assertEqual(add_operation(-2, -3), -5)

    def test_add_operation_mixed_numbers(self):
        self.assertEqual(add_operation(5, -3), 2)

    def test_subtract_operation_positive_numbers(self):
        self.assertEqual(subtract_operation(5, 2), 3)

    def test_subtract_operation_negative_numbers(self):
        self.assertEqual(subtract_operation(-5, -2), -3)

    def test_subtract_operation_mixed_numbers(self):
        self.assertEqual(subtract_operation(5, -2), 7)

if __name__ == '__main__':
    unittest.main()

