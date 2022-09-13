"""
test for adv_2021_04
"""

import unittest
import general_utils as gu
import solutions.adv_2021_04 as sol


def _data_small():
    return gu.read_input(4, "small")


def _data_p():
    return gu.read_input(4, "p")


def _data_m():
    return gu.read_input(4, "m")


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """

    def test_parse_input(self):
        """basic test of sol.parse_input"""
        numbers, data = sol.parse_input(_data_small())
        self.assertTrue(numbers)
        self.assertIn(",".join(str(_) for _ in numbers), _data_small())
        self.assertEqual(len(data), 3)

    def test_data_small(self):
        """test against the example data"""
        self.assertEqual(sol.solve_a(_data_small()), 4512)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 54275)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_m()), 65325)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """

    def test_data_small(self):
        """test against the example data"""
        self.assertEqual(sol.solve_b(_data_small()), 1924)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 13158)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_m()), 4624)


if __name__ == "__main__":
    unittest.main()
