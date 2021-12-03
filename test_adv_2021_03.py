"""
test for adv_2021_03
"""

import unittest
import adv_2021_03 as sol
import general_utils as gu

_TEST_DATA = \
    "00100\n" \
    "11110\n" \
    "10110\n" \
    "10101\n" \
    "01111\n" \
    "10111\n" \
    "00111\n" \
    "11100\n" \
    "10000\n" \
    "11001\n" \
    "00010\n" \
    "01010"

_DATA_P = gu.read_to_string('data_adv_2021_03_p.txt')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_basic(self):
        """test agains the example data"""
        self.assertEqual(sol.solve_a(_TEST_DATA), 198)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_DATA_P), 3009600)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_basic(self):
        """test agains the example data"""
        self.assertEqual(sol.solve_b(_TEST_DATA), 230)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_DATA_P), 6940518)


if __name__ == '__main__':
    unittest.main()
