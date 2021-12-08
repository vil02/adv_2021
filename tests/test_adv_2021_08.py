"""
test for adv_2021_template
"""

import unittest
import general_utils as gu
import solutions.adv_2021_08 as sol


def _data_small():
    return gu.read_input(8, 'small')


def _data_p():
    return gu.read_input(8, 'p')


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


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    # def test_evaluate(self):
    #     # def tested_fun(in_permutation, in_str):
    #     #     return sol.get_value(sol.apply_permutation(
    #     #         in_permutation, in_str.split(' ')))
    #     input_data = {
    #         'fdgacbe cefdb cefbgd gcbe': 8394,
    #         'fcgedb cgb dgebacf gc': 9781,
    #         'cg cg fdcagb cbg': 1197,
    #         'efabcd cedba gadfec cb': 9361,
    #         'gecf egdcabf bgf bfgea': 4873,
    #         'gebdcfa ecba ca fadegcb': 8418,
    #         'cefg dcbef fcge gbcadfe': 4548,
    #         'ed bcgafe cdgba cbgef': 1625,
    #         'gbdfcae bgc cg cgb': 8717,
    #         'fgae cfgab fg bagce': 4315}
    #     input_string = \
    #         'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'
    #     #permutation = sol.find_pemutation(input_string.split(' '))
    #     for (cur_str, cur_true_value) in input_data.items():
    #         print(cur_str)
    #         print(sol.find_pemutation(input_string.split()))
    #         self.assertEqual(
    #            sol.solve_single_line(input_string.split(), cur_str.split()), cur_true_value)


    def test_data_small(self):
        """test agains small data"""
        self.assertEqual(sol.solve_b(_data_small()), 61229)

    # def test_data_p(self):
    #     """test agains full data"""
    #     self.assertEqual(sol.solve_b(_data_p()), 1043101)


if __name__ == '__main__':
    unittest.main()
