"""
test for adv_2021_03
"""

import unittest
import general_utils as gu
import solutions.adv_2021_03 as sol

_TEST_DATA = [
    "00100",
    "11110",
    "10110",
    "10101",
    "01111",
    "10111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"]


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
        self.assertEqual(sol.calculate_gamma(_TEST_DATA), 22)

    def test_calculate_epsilon(self):
        """tests calculate_epsilon agains the example data"""
        self.assertEqual(sol.calculate_epsilon(_TEST_DATA), 9)

    def test_example_data(self):
        """tests solution function agains the example data"""
        self.assertEqual(sol.solve_a('\n'.join(_TEST_DATA)), 198)

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
        self.assertEqual(sol.calculate_oxygen(_TEST_DATA), 23)

    def test_calculate_co2(self):
        """tests calculate_epsilon agains the example data"""
        self.assertEqual(sol.calculate_co2(_TEST_DATA), 10)

    def test_example_data(self):
        """tests solution function agains the example data"""
        self.assertEqual(sol.solve_b('\n'.join(_TEST_DATA)), 230)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_p()), 6940518)

    def test_data_m(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_m()), 2775870)


if __name__ == '__main__':
    unittest.main()
