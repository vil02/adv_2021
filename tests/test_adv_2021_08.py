"""
test for adv_2021_template
"""

import unittest
import general_utils as gu
import solutions.adv_2021_08 as sol


def _data_small():
    return gu.read_input(8, 'small')


def _data_p():
    return gu.read_input(8, 'p')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_data_small(self):
        """test agains example data"""
        self.assertEqual(sol.solve_a(_data_small()), 26)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_p()), 445)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_small(self):
        """test agains small data"""
        self.assertEqual(sol.solve_b(_data_small()), 61229)

    # def test_data_p(self):
    #     """test agains full data"""
    #     self.assertEqual(sol.solve_b(_data_p()), 1043101)


if __name__ == '__main__':
    unittest.main()
