"""
test for adv_2021_20
"""

import unittest
import general_utils as gu
import solutions.adv_2021_20 as sol


def _data_p():
    return gu.read_input(20, 'p')


def _data_small():
    return gu.read_input(20, 'small')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_get_all_neighbours(self):
        """test of get_all_neighbours function"""
        test_pos = (1, 3)
        true_res = (
            (0, 4), (1, 4), (2, 4),
            (0, 3), (1, 3), (2, 3),
            (0, 2), (1, 2), (2, 2))
        self.assertIn(test_pos, true_res)
        self.assertEqual(sol.get_all_neighbours(test_pos), true_res)

    def test_parse_input(self):
        """test of the parse_input function against the example data"""
        alg_data, _ = sol.parse_input(_data_small())
        self.assertIn(34, alg_data)
        self.assertIn(511, alg_data)
        self.assertNotIn(0, alg_data)
        self.assertNotIn(1, alg_data)
        self.assertIn(2, alg_data)

    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_a(_data_small()), 35)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 4928)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_small(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_small()), 3351)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 16605)


if __name__ == '__main__':
    unittest.main()
