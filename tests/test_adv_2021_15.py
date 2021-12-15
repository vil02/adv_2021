"""
test for adv_2021_15
"""

import unittest
import general_utils as gu
import solutions.adv_2021_15 as sol


def _data_small():
    return gu.read_input(15, 'small')


def _data_p():
    return gu.read_input(15, 'p')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_data_small(self):
        """test agains example data"""
        self.assertEqual(sol.solve_a(_data_small()), 40)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_p()), 714)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_small(self):
        """test agains example data"""
        self.assertEqual(sol.solve_b(_data_small()), 315)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_p()), 2948)


if __name__ == '__main__':
    unittest.main()
