"""
test for adv_2021_template
"""

import unittest
import adv_2021_04 as sol
import general_utils as gu

_DATA_SMALL = gu.read_to_string('data_adv_2021_04_small.txt')
_DATA_P = gu.read_to_string('data_adv_2021_04_p.txt')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    # def test_basic(self):
    #     """test agains the example data"""
    #     pass
    #
    def test_data_small(self):
        """test agains the example data"""
        self.assertEqual(sol.solve_a(_DATA_SMALL), 4512)


    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_DATA_P), 54275)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_small(self):
        """test agains the example data"""
        self.assertEqual(sol.solve_b(_DATA_SMALL), 1924)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_DATA_P), 13158)


if __name__ == '__main__':
    unittest.main()
