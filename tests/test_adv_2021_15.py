"""
test for adv_2021_15
"""

import unittest
import general_utils as gu
import solutions.adv_2021_15 as sol


def _data_small():
    return gu.read_input(15, 'small')


def _data_small_b():
    return gu.read_input(15, 'small_b')


def _data_other():
    return gu.read_input(15, 'other')


def _data_p():
    return gu.read_input(15, 'p')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_a(_data_small()), 40)

    def test_data_small_b(self):
        """test against extented example data"""
        self.assertEqual(sol.solve_a(_data_small_b()), 315)

    def test_data_other(self):
        """test against data with the minimal path going left or up"""
        self.assertEqual(sol.solve_a(_data_other()), 12)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 714)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_extend_data(self):
        """test of extend_data"""
        self.assertEqual(
            sol.extend_data(sol.parse_input(_data_small())),
            sol.parse_input(_data_small_b()))

    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_b(_data_small()), 315)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 2948)


if __name__ == '__main__':
    unittest.main()
