"""
test for adv_2021_01
"""

import unittest
import general_utils as gu
import solutions.adv_2021_01 as sol

_DAY_NUM = 1


def _data_p():
    return gu.read_input(_DAY_NUM, "p")


def _data_m():
    return gu.read_input(_DAY_NUM, "m")


def _data_s():
    return gu.read_input(_DAY_NUM, "s")


def _data_t():
    return gu.read_input(_DAY_NUM, "t")


def _data_a():
    return gu.read_input(_DAY_NUM, "a")


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """

    def test_basic(self):
        """test against the example data"""
        test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(sol.count_a(test_data), 7)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 1548)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_m()), 1448)

    def test_data_s(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_s()), 1527)

    def test_data_t(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_t()), 1316)

    def test_data_a(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_a()), 1532)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """

    def test_basic(self):
        """test against the example data"""
        test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(sol.count_b(test_data), 5)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 1589)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_m()), 1471)

    def test_data_s(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_s()), 1575)

    def test_data_t(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_t()), 1344)

    def test_data_a(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_a()), 1571)


if __name__ == "__main__":
    unittest.main()
