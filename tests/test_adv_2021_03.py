"""
test for adv_2021_03
"""

import unittest
import general_utils as gu
import solutions.adv_2021_03 as sol


def _read_input(input_id):
    return gu.read_input(3, input_id)


def _data_small():
    return _read_input("small")


def _data_p():
    return _read_input("p")


def _data_m():
    return _read_input("m")


def _data_s():
    return _read_input("s")


def _data_t():
    return _read_input("t")


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """

    def test_calculate_gamma(self):
        """tests calculate_gamma against the example data"""
        self.assertEqual(sol.calculate_gamma(_data_small().split()), 22)

    def test_calculate_epsilon(self):
        """tests calculate_epsilon against the example data"""
        self.assertEqual(sol.calculate_epsilon(_data_small().split()), 9)

    def test_example_data(self):
        """tests solution function against the example data"""
        self.assertEqual(sol.solve_a(_data_small()), 198)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 3009600)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_m()), 2724524)

    def test_data_s(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_s()), 1540244)

    def test_data_t(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_t()), 2003336)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """

    def test_calculate_oxygen(self):
        """tests calculate_gamma against the example data"""
        self.assertEqual(sol.calculate_oxygen(_data_small().split()), 23)

    def test_calculate_co2(self):
        """tests calculate_epsilon against the example data"""
        self.assertEqual(sol.calculate_co2(_data_small().split()), 10)

    def test_example_data(self):
        """tests solution function against the example data"""
        self.assertEqual(sol.solve_b(_data_small()), 230)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 6940518)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_m()), 2775870)

    def test_data_s(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_s()), 4203981)

    def test_data_t(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_t()), 1877139)


if __name__ == "__main__":
    unittest.main()
