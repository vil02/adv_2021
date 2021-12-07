"""
test for adv_2021_07
"""

import unittest
import general_utils as gu
import solutions.adv_2021_07 as sol


def _data_small():
    return '16,1,2,0,4,2,7,1,2,14'


def _data_p():
    return gu.read_input(7, 'p')


def _data_m():
    return gu.read_input(7, 'm')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_parse_input(self):
        """test parse_input agains the example data"""
        self.assertEqual(
            sol.parse_input(_data_small()), [16, 1, 2, 0, 4, 2, 7, 1, 2, 14])

    def test_data_small(self):
        """test agains the example data"""
        self.assertEqual(sol.solve_a(_data_small()), 37)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_p()), 328262)

    def test_data_m(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_m()), 335271)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_small(self):
        """test agains the example data"""
        self.assertEqual(sol.solve_b(_data_small()), 168)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_p()), 90040997)

    def test_data_m(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_m()), 95851339)


if __name__ == '__main__':
    unittest.main()
