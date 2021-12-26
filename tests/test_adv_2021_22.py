"""
test for adv_2021_22
"""

import unittest
import general_utils as gu
import solutions.adv_2021_22 as sol


def _data_p():
    return gu.read_input(22, 'p')


def _data_very_small():
    return gu.read_input(22, 'very_small')


def _data_small():
    return gu.read_input(22, 'small')


def _data_small_b():
    return gu.read_input(22, 'small_b')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_data_very_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_a(_data_very_small()), 39)

    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_a(_data_small()), 590784)

    def test_data_small_b(self):
        """test against example data"""
        self.assertEqual(sol.solve_a(_data_small_b()), 474140)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 553201)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_very_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_b(_data_very_small()), 39)

    def test_data_small_b(self):
        """test against example data"""
        self.assertEqual(sol.solve_b(_data_small_b()), 2758514936282235)

#    def test_data_p(self):
#        """test against full data"""
#        self.assertEqual(sol.solve_b(_data_p()), 1263946820845866)


if __name__ == '__main__':
    unittest.main()
