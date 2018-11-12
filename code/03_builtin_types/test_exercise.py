from unittest import TestCase
from .exercise import get_odd_squares_list, get_word_count_dict


class TestExercise(TestCase):
    def test_get_odd_squares_list(self):
        values = get_odd_squares_list(range(4))

        self.assertListEqual(values, [
            (0, 0),
            (2, 4)
        ])

    def test_get_word_count_dict(self):
        word_counts = get_word_count_dict("dog cat dog chicken")

        self.assertDictEqual(word_counts, {
            "dog": 2,
            "cat": 1,
            "chicken": 1
        })
