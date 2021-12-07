"""
test for adv_2021_07
"""

import unittest
import adv_2021_07 as sol
import general_utils as gu

_DATA_SMALL = '16,1,2,0,4,2,7,1,2,14'
_DATA_P = gu.read_to_string('data_adv_2021_07_p.txt')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_parse_input(self):
        """test parse_input agains the example data"""
        self.assertEqual(
            sol.parse_input(_DATA_SMALL), [16, 1, 2, 0, 4, 2, 7, 1, 2, 14])

    def test_data_small(self):
        """test agains the example data"""
        self.assertEqual(sol.solve_a(_DATA_SMALL), 37)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_DATA_P), 328262)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_small(self):
        """test agains the example data"""
        self.assertEqual(sol.solve_b(_DATA_SMALL), 168)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_DATA_P), 90040997)


if __name__ == '__main__':
    unittest.main()
