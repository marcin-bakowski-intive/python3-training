from unittest import TestCase

from excercises.fibonacci import get_fibonacci_nth_value


class FibonacciTest(TestCase):
    def test_fibonacci_sequence(self):
        self.assertEqual(get_fibonacci_nth_value(0), 0)
        self.assertEqual(get_fibonacci_nth_value(1), 1)
        self.assertEqual(get_fibonacci_nth_value(2), 1)
        self.assertEqual(get_fibonacci_nth_value(3), 2)
        self.assertEqual(get_fibonacci_nth_value(4), 3)
        self.assertEqual(get_fibonacci_nth_value(5), 5)
        self.assertEqual(get_fibonacci_nth_value(6), 8)
