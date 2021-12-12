"""
test for adv_2021_12
"""

import unittest
import general_utils as gu
import solutions.adv_2021_12 as sol


def _data_p():
    return gu.read_input(12, 'p')


def _data_small():
    return gu.read_input(12, 'small')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_data_small(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_small()), 226)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_p()), 3708)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_small(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_small()), 3509)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_p()), 93858)


if __name__ == '__main__':
    unittest.main()
