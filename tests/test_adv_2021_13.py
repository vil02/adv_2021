"""
test for adv_2021_13
"""

import unittest
import general_utils as gu
import solutions.adv_2021_13 as sol


def _data_small():
    return gu.read_input(13, 'small')


def _data_small_result():
    return gu.read_input(13, 'small_result').strip()


def _data_p():
    return gu.read_input(13, 'p')


def _data_p_result():
    return gu.read_input(13, 'p_result').strip()


def _data_m():
    return gu.read_input(13, 'm')


def _data_m_result():
    return gu.read_input(13, 'm_result').strip()


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_data_small(self):
        """test agains example data"""
        self.assertEqual(sol.solve_a(_data_small()), 17)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_p()), 638)

    def test_data_m(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_m()), 847)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_small(self):
        """test example full data"""
        self.assertEqual(sol.solve_b(_data_small()), _data_small_result())

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_p()), _data_p_result())

    def test_data_m(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_m()), _data_m_result())


if __name__ == '__main__':
    unittest.main()
