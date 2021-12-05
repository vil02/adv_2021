"""
test for adv_2021_05
"""

import unittest
import adv_2021_05 as sol
import general_utils as gu

_DATA_P = gu.read_to_string('data_adv_2021_05_p.txt')
_DATA_SMALL = gu.read_to_string('data_adv_2021_05_small.txt')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_data_small(self):
        """test agains example data"""
        self.assertEqual(sol.solve_a(_DATA_SMALL), 5)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_DATA_P), 4873)
        # not 3223
        # not 9811


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_small(self):
        """test agains example data"""
        self.assertEqual(sol.solve_b(_DATA_SMALL), 12)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_DATA_P), 19472)


if __name__ == '__main__':
    unittest.main()
