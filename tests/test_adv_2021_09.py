"""
test for adv_2021_09
"""

import unittest
import general_utils as gu
import solutions.adv_2021_09 as sol


def _data_small():
    return gu.read_input(9, 'small')


def _data_p():
    return gu.read_input(9, 'p')


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


if __name__ == '__main__':
    unittest.main()
