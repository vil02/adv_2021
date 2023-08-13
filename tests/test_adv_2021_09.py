"""
test for adv_2021_09
"""

import unittest
import general_utils as gu
import solutions.adv_2021_09 as sol


def _read_input(input_id):
    return gu.read_input(9, input_id)


def _data_small():
    return _read_input("small")


def _data_p():
    return _read_input("p")


def _data_m():
    return _read_input("m")


def _data_s():
    return _read_input("s")


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """

    def test_get_adjacent_values(self):
        """
        test of get_adjacent_values
        """
        data = sol.parse_input(_data_small())
        self.assertEqual(set(sol.get_adjacent_values(data, (0, 0))), {1, 3})
        self.assertEqual(set(sol.get_adjacent_values(data, (2, 1))), {5, 7, 9})

    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_a(_data_small()), 15)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 516)

    def test_data_s(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_s()), 491)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """

    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_b(_data_small()), 1134)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 1023660)

    def test_data_s(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_s()), 1075536)


if __name__ == "__main__":
    unittest.main()
