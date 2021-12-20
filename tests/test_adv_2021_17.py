"""
test for adv_2021_17
"""

import unittest
import general_utils as gu  # noqa # pylint: disable=unused-import
import solutions.adv_2021_17 as sol


def _data_small():
    return ((20, 30), (-10, -5))


def _data_p():
    return ((156, 202), (-110, -69))


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_data_small(self):
        """test agains example data"""
        self.assertEqual(sol.solve_a(_data_small()), 45)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_p()), 5995)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_small(self):
        """test agains example data"""
        self.assertEqual(sol.solve_b(_data_small()), 112)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_p()), 3202)


if __name__ == '__main__':
    unittest.main()
