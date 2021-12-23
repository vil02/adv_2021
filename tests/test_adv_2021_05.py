"""
test for adv_2021_05
"""

import unittest
import general_utils as gu
import solutions.adv_2021_05 as sol


def _data_small():
    return gu.read_input(5, 'small')


def _data_p():
    return gu.read_input(5, 'p')


def _data_m():
    return gu.read_input(5, 'm')


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


if __name__ == '__main__':
    unittest.main()
