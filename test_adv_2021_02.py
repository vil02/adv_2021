"""
test for adv_2021_02
"""

import unittest
import adv_2021_02 as sol
import general_utils as gu

_TEST_STR = \
    "forward 5\n" \
    "down 5\n" \
    "forward 8\n" \
    "up 3\n" \
    "down 8\n" \
    "forward 2"

_DATA_P = gu.read_to_string('data_adv_2021_02_p.txt')
_DATA_M = gu.read_to_string('data_adv_2021_02_m.txt')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_basic(self):
        """test agains the example data"""
        self.assertEqual(
            sol.solve_a(_TEST_STR),
            150)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_DATA_P), 1524750)

    def test_data_m(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_DATA_M), 1507611)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_basic(self):
        """test agains the example data"""
        self.assertEqual(
            sol.solve_b(_TEST_STR),
            900)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_DATA_P), 1592426537)

    def test_data_m(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_DATA_M), 1880593125)


if __name__ == '__main__':
    unittest.main()
