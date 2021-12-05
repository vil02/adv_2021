"""
test for adv_2021_05
"""

import unittest
import adv_2021_05 as sol
import general_utils as gu


_DATA_SMALL, _DATA_P, _DATA_M = [
    gu.read_to_string(f'data_adv_2021_05_{_}.txt') for
    _ in ['small', 'p', 'm']]


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

    def test_data_m(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_DATA_M), 3990)


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

    def test_data_m(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_DATA_M), 21305)


if __name__ == '__main__':
    unittest.main()
