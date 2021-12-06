"""
test for adv_2021_06
"""

import unittest
import adv_2021_06 as sol
import general_utils as gu

_DATA_P = gu.read_to_string('data_adv_2021_06_p.txt')
_DATA_M = gu.read_to_string('data_adv_2021_06_m.txt')
_DATA_SMALL = '3,4,3,1,2'


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_parse_input(self):
        """tests parse_input function"""
        self.assertEqual(sol.parse_input(_DATA_SMALL), [3, 4, 3, 1, 2])

    def test_count_number_of_all_fish(self):
        """tests count_number_of_all_fish function with example data"""
        self.assertEqual(
            sol.count_number_of_all_fish(sol.parse_input(_DATA_SMALL), 18),
            26)

    def test_basic(self):
        """test agains the example data"""
        self.assertEqual(sol.solve_a(_DATA_SMALL), 5934)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_DATA_P), 380612)

    def test_data_m(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_DATA_M), 362740)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_basic(self):
        """test agains the example data"""
        self.assertEqual(sol.solve_b(_DATA_SMALL), 26984457539)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_DATA_P), 1710166656900)

    def test_data_m(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_DATA_M), 1644874076764)


if __name__ == '__main__':
    unittest.main()
