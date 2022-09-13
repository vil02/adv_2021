"""
test for adv_2021_02
"""

import unittest
import general_utils as gu
import solutions.adv_2021_02 as sol


def _data_small():
    return gu.read_input(2, "small")


def _data_p():
    return gu.read_input(2, "p")


def _data_m():
    return gu.read_input(2, "m")


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """

    def test_basic(self):
        """test against the example data"""
        self.assertEqual(sol.solve_a(_data_small()), 150)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 1524750)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_m()), 1507611)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """

    def test_basic(self):
        """test against the example data"""
        self.assertEqual(sol.solve_b(_data_small()), 900)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 1592426537)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_m()), 1880593125)


if __name__ == "__main__":
    unittest.main()
