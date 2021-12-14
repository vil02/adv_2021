"""
test for adv_2021_14
"""
# import sys
# sys.setrecursionlimit(1600)

import unittest
import general_utils as gu
import solutions.adv_2021_14 as sol


def _data_small():
    return gu.read_input(14, 'small')


def _data_p():
    return gu.read_input(14, 'p')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_data_small(self):
        """test agains example data"""
        self.assertEqual(sol.solve_a(_data_small()), 1588)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_p()), 3247)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_small(self):
        """test agains example data"""
        self.assertEqual(sol.solve_b(_data_small()), 2188189693529)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_p()), 4110568157153)


if __name__ == '__main__':
    unittest.main()
