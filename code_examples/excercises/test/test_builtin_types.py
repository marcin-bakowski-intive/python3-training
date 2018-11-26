from unittest import TestCase

from excercises.builtin_types import round_2_points_precision


class BuiltinTypeTest(TestCase):
    def test_round_2_points_precision(self):
        self.assertEqual(round_2_points_precision("123.111111"), 123.11)
