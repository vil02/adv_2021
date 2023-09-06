"""
test for adv_2021_06
"""

import unittest
import general_utils as gu
import solutions.adv_2021_06 as sol


def _data_small():
    return "3,4,3,1,2"


def _read_input(input_id):
    return gu.read_input(6, input_id)


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

    def test_parse_input(self):
        """tests parse_input function"""
        self.assertEqual(sol.parse_input(_data_small()), [3, 4, 3, 1, 2])

    def test_count_number_of_all_fish(self):
        """tests count_number_of_all_fish function with example data"""
        self.assertEqual(
            sol.count_number_of_all_fish(sol.parse_input(_data_small()), 18), 26
        )

    def test_basic(self):
        """test against the example data"""
        self.assertEqual(sol.solve_a(_data_small()), 5934)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 380612)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_m()), 362740)

    def test_data_s(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_s()), 358214)

    def test_data_t(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_t()), 377263)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """

    def test_basic(self):
        """test against the example data"""
        self.assertEqual(sol.solve_b(_data_small()), 26984457539)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 1710166656900)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_m()), 1644874076764)

    def test_data_s(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_s()), 1622533344325)

    def test_data_t(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_t()), 1695929023803)


if __name__ == "__main__":
    unittest.main()
