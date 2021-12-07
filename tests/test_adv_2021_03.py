"""
test for adv_2021_03
"""

import unittest
import general_utils as gu
import solutions.adv_2021_03 as sol


def _data_small():
    return gu.read_input(3, 'small')


def _data_p():
    return gu.read_input(3, 'p')


def _data_m():
    return gu.read_input(3, 'm')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_calculate_gamma(self):
        """tests calculate_gamma agains the example data"""
        self.assertEqual(sol.calculate_gamma(_data_small().split()), 22)

    def test_calculate_epsilon(self):
        """tests calculate_epsilon agains the example data"""
        self.assertEqual(sol.calculate_epsilon(_data_small().split()), 9)

    def test_example_data(self):
        """tests solution function agains the example data"""
        self.assertEqual(sol.solve_a(_data_small()), 198)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_p()), 3009600)

    def test_data_m(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_m()), 2724524)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_calculate_oxygen(self):
        """tests calculate_gamma agains the example data"""
        self.assertEqual(sol.calculate_oxygen(_data_small().split()), 23)

    def test_calculate_co2(self):
        """tests calculate_epsilon agains the example data"""
        self.assertEqual(sol.calculate_co2(_data_small().split()), 10)

    def test_example_data(self):
        """tests solution function agains the example data"""
        self.assertEqual(sol.solve_b(_data_small()), 230)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_p()), 6940518)

    def test_data_m(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_m()), 2775870)


if __name__ == '__main__':
    unittest.main()
