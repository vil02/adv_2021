"""
test for adv_2021_07
"""

import unittest
import general_utils as gu
import solutions.adv_2021_07 as sol


def _data_small():
    return "16,1,2,0,4,2,7,1,2,14"


def _read_input(input_id):
    return gu.read_input(7, input_id)


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

    def test_parse_input(self):
        """test parse_input against the example data"""
        self.assertEqual(
            sol.parse_input(_data_small()), [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        )

    def test_data_small(self):
        """test against the example data"""
        self.assertEqual(sol.solve_a(_data_small()), 37)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 328262)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_m()), 335271)

    def test_data_s(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_s()), 356922)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """

    def test_data_small(self):
        """test against the example data"""
        self.assertEqual(sol.solve_b(_data_small()), 168)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 90040997)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_m()), 95851339)

    def test_data_s(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_s()), 100347031)


if __name__ == "__main__":
    unittest.main()
