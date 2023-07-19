"""
test for adv_2021_02
"""

import unittest
import general_utils as gu
import solutions.adv_2021_02 as sol


def _read_input(input_id):
    return gu.read_input(2, input_id)


def _data_small():
    return _read_input("small")


def _data_p():
    return _read_input("p")


def _data_m():
    return _read_input("m")


def _data_s():
    return _read_input("s")


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

    def test_data_s(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_s()), 2036120)


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

    def test_data_s(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_s()), 2015547716)


if __name__ == "__main__":
    unittest.main()
