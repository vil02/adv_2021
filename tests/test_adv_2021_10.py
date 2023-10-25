"""
test for adv_2021_10
"""

import unittest
import general_utils as gu
import solutions.adv_2021_10 as sol


def _data_small():
    return gu.read_input(10, "small")


def _data_p():
    return gu.read_input(10, "p")


def _data_m():
    return gu.read_input(10, "m")


def _data_t():
    return gu.read_input(10, "t")


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """

    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_a(_data_small()), 26397)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 311895)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_m()), 168417)

    def test_data_t(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_t()), 369105)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """

    def test_find_line_completion(self):
        """tests find_line_completion against example data"""
        input_data = {
            "[({(<(())[]>[[{[]{<()<>>": "}}]])})]",
            "[(()[<>])]({[<{<<[]>>(": ")}>]})",
            "(((({<>}<{<{<>}{[]{[]{}": "}}>}>))))",
            "{<[[]]>}<{[{[{[]{()[[[]": "]]}}]}]}>",
            "<{([{{}}[<[[[<>{}]]]>[]]": "])}>",
        }
        for (test_input, res) in input_data.items():
            self.assertEqual(sol.find_line_completion(test_input), res)

    def test_get_completion_score(self):
        """tests get_completion_score against example data"""
        input_data = {
            "}}]])})]": 288957,
            ")}>]})": 5566,
            "}}>}>))))": 1480781,
            "]]}}]}]}>": 995444,
            "])}>": 294,
        }
        for (test_input, res) in input_data.items():
            self.assertEqual(sol.get_completion_score(test_input), res)

    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_b(_data_small()), 288957)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 2904180541)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_m()), 2802519786)

    def test_data_t(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_t()), 3999363569)


if __name__ == "__main__":
    unittest.main()
