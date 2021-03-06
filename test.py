import unittest

import argparse

import sum_sequence


class TestPositiveInteger(unittest.TestCase):
    def test_negative(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            sum_sequence.positive_integer('-1')

    def test_zero(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            sum_sequence.positive_integer('0')

    def test_non_integer(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            sum_sequence.positive_integer('a')

    def test_integer(self):
        self.assertEqual(sum_sequence.positive_integer('1'), 1)


class TestSumSequence(unittest.TestCase):

    def test_zero(self):
        with self.assertRaises(AssertionError):
            list(sum_sequence.generate_sequence(0))

    def test_negative(self):
        with self.assertRaises(AssertionError):
            list(sum_sequence.generate_sequence(-1))

    def test_1(self):
        results = list(sum_sequence.generate_sequence(1))
        self.assertEqual(results, [[1]])

    def test_2(self):
        results = list(sum_sequence.generate_sequence(2))
        self.assertIn([2], results)
        self.assertIn([1, 1], results)
        self.assertEqual(len(results), 2)

    def test_5(self):
        results = list(sum_sequence.generate_sequence(5))
        self.assertIn([5], results)
        self.assertIn([4, 1], results)
        self.assertIn([3, 2], results)
        self.assertIn([3, 1, 1], results)
        self.assertIn([2, 2, 1], results)
        self.assertIn([2, 1, 1, 1], results)
        self.assertIn([1, 1, 1, 1, 1], results)
        self.assertEqual(len(results), 7)

    def test_7(self):
        results = list(sum_sequence.generate_sequence(7))
        self.assertIn([7], results)
        self.assertIn([6, 1], results)
        self.assertIn([5, 2], results)
        self.assertIn([5, 1, 1], results)
        self.assertIn([4, 3], results)
        self.assertIn([4, 2, 1], results)
        self.assertIn([4, 1, 1, 1], results)
        self.assertIn([3, 3, 1], results)
        self.assertIn([3, 2, 2], results)
        self.assertIn([3, 2, 1, 1], results)
        self.assertIn([3, 1, 1, 1, 1], results)
        self.assertIn([2, 2, 2, 1], results)
        self.assertIn([2, 2, 1, 1, 1], results)
        self.assertIn([2, 1, 1, 1, 1, 1], results)
        self.assertIn([1, 1, 1, 1, 1, 1, 1], results)
        self.assertEqual(len(results), 15)

if __name__ == '__main__':
    unittest.main()
