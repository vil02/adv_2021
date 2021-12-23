"""
test for adv_2021_23
"""

import unittest
import general_utils as gu
# import solutions.adv_2021_23 as sol


def _data_small():
    return gu.read_input(23, 'small')


def _data_p():
    return gu.read_input(23, 'p')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
#    def test_data_small(self):
#        """test against example data"""
#        self.assertEqual(sol.solve_a(_data_small()), 12521)
#
#    def test_data_p(self):
#        """test against full data"""
#        self.assertEqual(sol.solve_a(_data_p()), 11120)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
#    def test_data_small(self):
#        """test against example data"""
#        self.assertEqual(sol.solve_b(_data_small()), 44169)
#
#    def test_data_p(self):
#        """test against full data"""
#        self.assertEqual(sol.solve_b(_data_p()), 49232)


if __name__ == '__main__':
    unittest.main()
