"""
test for adv_2021_08
"""

import unittest
import general_utils as gu
import solutions.adv_2021_08 as sol


def _read_input(input_id):
    return gu.read_input(8, input_id)


def _data_small():
    return _read_input("small")


def _data_p():
    return _read_input("p")


def _data_m():
    return _read_input("m")


def _data_s():
    return _read_input("s")


def _data_t():
    return _read_input("t")


def _data_a():
    return _read_input("a")


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """

    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_a(_data_small()), 26)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 445)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_m()), 294)

    def test_data_s(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_s()), 440)

    def test_data_t(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_t()), 387)

    def test_data_a(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_a()), 318)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """

    def test_small_example(self):
        """test against small example in part b"""
        input_string = (
            "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"
        )
        permutation = sol.find_pemutation(input_string.split(" "))

        def get_value(in_str):
            return sol.get_value(
                sol.apply_permutation(permutation, in_str.split())
            )

        self.assertEqual(get_value(input_string), 8523796401)
        self.assertEqual(get_value("cdfeb fcadb cdfeb cdbaf"), 5353)

    def test_data_small(self):
        """test against small data"""
        self.assertEqual(sol.solve_b(_data_small()), 61229)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 1043101)

    def test_data_m(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_m()), 973292)

    def test_data_s(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_s()), 1046281)

    def test_data_t(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_t()), 986034)

    def test_data_a(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_a()), 996280)


if __name__ == "__main__":
    unittest.main()
