"""
test for adv_2021_05
"""

import unittest
import general_utils as gu
import solutions.adv_2021_05 as sol


def _read_input(input_id):
    return gu.read_input(5, input_id)


def _data_small():
    return _read_input("small")


def _data_p():
    return _read_input("p")


def _data_m():
    return _read_input("m")


def _data_s():
    return _read_input("s")


def _data_t():
    return _read_input("t")


def _data_a():
    return _read_input("a")


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """

    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_a(_data_small()), 5)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 4873)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_m()), 3990)

    def test_data_s(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_s()), 7473)

    def test_data_t(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_t()), 6397)

    def test_data_a(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_a()), 6113)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """

    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_b(_data_small()), 12)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 19472)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_m()), 21305)

    def test_data_s(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_s()), 24164)

    def test_data_t(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_t()), 22335)

    def test_data_a(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_a()), 20373)


if __name__ == "__main__":
    unittest.main()
