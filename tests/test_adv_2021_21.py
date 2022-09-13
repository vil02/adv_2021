"""
test for adv_2021_template
"""

import unittest
import general_utils as gu
import solutions.adv_2021_21 as sol


def _data_p():
    return gu.read_input(21, "p")


def _data_small():
    return gu.read_input(21, "small")


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """

    def test_data_small(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_small()), 739785)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 742257)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """

    def test_data_small(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_small()), 444356092776315)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 93726416205179)


if __name__ == "__main__":
    unittest.main()
