"""
test for adv_2021_17
"""

import unittest
import general_utils as gu
import solutions.adv_2021_17 as sol


def _data_small():
    return gu.read_input(17, 'small')


def _data_p():
    return gu.read_input(17, 'p')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    # def test_data_p(self):
    #     """test agains full data"""
    #     self.assertEqual(sol.solve_a(_data_p()), 5995)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_p()), 3202)


if __name__ == '__main__':
    unittest.main()
