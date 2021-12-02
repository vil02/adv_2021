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
        self.assertEqual(
            sol.solve_a(gu.read_to_string('data_adv_2021_02_p.txt')),
            1524750)


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
        self.assertEqual(
            sol.solve_b(gu.read_to_string('data_adv_2021_02_p.txt')),
            1592426537)


if __name__ == '__main__':
    unittest.main()
