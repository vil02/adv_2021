"""
test for adv_2021_08
"""

import unittest
import general_utils as gu
import solutions.adv_2021_08 as sol


def _data_small():
    return gu.read_input(8, 'small')


def _data_p():
    return gu.read_input(8, 'p')


def _data_m():
    return gu.read_input(8, 'm')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_data_small(self):
        """test agains example data"""
        self.assertEqual(sol.solve_a(_data_small()), 26)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_p()), 445)

    def test_data_m(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_m()), 294)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_small_example(self):
        """test against small example in part b"""
        input_string = \
            'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'
        permutation = sol.find_pemutation(input_string.split(' '))

        def get_value(in_str):
            return sol.get_value(sol.apply_permutation(
                permutation, in_str.split()))
        self.assertEqual(get_value(input_string), 8523796401)
        self.assertEqual(get_value('cdfeb fcadb cdfeb cdbaf'), 5353)

    def test_data_small(self):
        """test agains small data"""
        self.assertEqual(sol.solve_b(_data_small()), 61229)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_p()), 1043101)

    def test_data_m(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_m()), 973292)


if __name__ == '__main__':
    unittest.main()
