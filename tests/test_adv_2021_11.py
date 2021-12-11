"""
test for adv_2021_11
"""

import unittest
import general_utils as gu
import solutions.adv_2021_11 as sol


def _data_very_small():
    return gu.read_input(11, 'very_small')


def _data_small():
    return gu.read_input(11, 'small')


def _data_p():
    return gu.read_input(11, 'p')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_single_step_very_small(self):
        """tests single_step function with the very small example data"""
        data = sol.parse_input(_data_very_small())
        data, number_of_flashes = sol.single_step(data)
        self.assertEqual(number_of_flashes, 9)
        data, number_of_flashes = sol.single_step(data)
        self.assertEqual(number_of_flashes, 0)

    def test_data_small(self):
        """test agains small data"""
        self.assertEqual(sol.solve_a(_data_small()), 1656)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_p()), 1667)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_small(self):
        """test agains small data"""
        self.assertEqual(sol.solve_b(_data_small()), 195)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_p()), 488)


if __name__ == '__main__':
    unittest.main()
