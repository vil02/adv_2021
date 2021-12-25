"""
test for adv_2021_25s
"""

import unittest
import general_utils as gu
import solutions.adv_2021_25 as sol


def _data_p():
    return gu.read_input(25, 'p')


def _data_small():
    return gu.read_input(25, 'small')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_a(_data_small()), 58)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 419)


if __name__ == '__main__':
    unittest.main()
