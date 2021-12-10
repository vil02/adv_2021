"""
test for adv_2021_10
"""

import unittest
import general_utils as gu
import solutions.adv_2021_10 as sol


def _data_small():
    return gu.read_input(10, 'small')


def _data_p():
    return gu.read_input(10, 'p')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_data_small(self):
        """test agains example data"""
        self.assertEqual(sol.solve_a(_data_small()), 26397)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_p()), 311895)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_find_line_completion(self):
        """tests find_line_completion agains example data"""
        input_data = {
            '[({(<(())[]>[[{[]{<()<>>': '}}]])})]',
            '[(()[<>])]({[<{<<[]>>(': ')}>]})',
            '(((({<>}<{<{<>}{[]{[]{}': '}}>}>))))',
            '{<[[]]>}<{[{[{[]{()[[[]': ']]}}]}]}>',
            '<{([{{}}[<[[[<>{}]]]>[]]': '])}>'}
        for (test_input, res) in input_data.items():
            self.assertEqual(sol.find_line_completion(test_input), res)

    def test_get_completion_score(self):
        """tests get_completion_score agains example data"""
        input_data = {
            '}}]])})]': 288957,
            ')}>]})': 5566,
            '}}>}>))))': 1480781,
            ']]}}]}]}>': 995444,
            '])}>': 294}
        for (test_input, res) in input_data.items():
            self.assertEqual(sol.get_completion_score(test_input), res)

    def test_data_small(self):
        """test agains example data"""
        self.assertEqual(sol.solve_b(_data_small()), 288957)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_p()), 2904180541)


if __name__ == '__main__':
    unittest.main()
