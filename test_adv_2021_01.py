"""
test for adv_2021_01
"""

import unittest
import adv_2021_01 as sol
import general_utils as gu


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_basic(self):
        """test agains the example data"""
        test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(sol.count_a(test_data), 7)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(
            sol.solve_a(gu.read_to_string('data_adv_2021_01_p.txt')),
            1548)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_basic(self):
        """test agains the example data"""
        test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(sol.count_b(test_data), 5)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(
            sol.solve_b(gu.read_to_string('data_adv_2021_01_p.txt')),
            1589)


if __name__ == '__main__':
    unittest.main()
