"""
test for adv_2021_24
"""

import unittest
import general_utils as gu
import solutions.adv_2021_24 as sol


def _data_p():
    return gu.read_input(24, "p")


def _data_o_1():
    return gu.read_input(24, "o_1")


def _data_o_2():
    return gu.read_input(24, "o_2")


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 99919765949498)

    def test_data_o_1(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_o_1()), 92969593497992)

    def test_data_o_2(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_o_2()), 99893999291967)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 24913111616151)

    def test_data_o_1(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_o_1()), 81514171161381)

    def test_data_o_2(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_o_2()), 34171911181211)


if __name__ == "__main__":
    unittest.main()
