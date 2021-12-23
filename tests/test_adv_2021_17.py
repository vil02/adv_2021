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


def _data_o():
    return ((57, 116), (-198, -148))


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_a(_data_small()), 45)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 5995)

    def test_data_o(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_o()), 19503)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_b(_data_small()), 112)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 3202)

    def test_data_o(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_o()), 5200)


if __name__ == '__main__':
    unittest.main()
