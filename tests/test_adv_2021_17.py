"""
test for adv_2021_17
"""

import unittest
import solutions.adv_2021_17 as sol


def _data_small():
    return ((20, 30), (-10, -5))


def _data_p():
    return ((156, 202), (-110, -69))


def _data_o():
    return ((57, 116), (-198, -148))


def _data_t():
    return ((14, 50), (-267, -225))


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """

    def test_get_next_state_x_negative_vel(self):
        """
        test of the function get_next_state_x with in_vel_x being negative
        """
        new_pos, new_vel = sol.get_next_state_x(10, -5)
        self.assertEqual(new_pos, 5)
        self.assertEqual(new_vel, -4)

    def test_positive_is_hit_x_zero_vel(self):
        """positive test of is_hit_x with in_vel_x being 0"""
        target_data = (5, 10)
        for _ in range(target_data[0], target_data[1] + 1):
            self.assertTrue(sol.is_hit_x(_, 0, target_data))

    def test_negative_is_hit_x_zero_vel(self):
        """negative test of is_hit_x with in_vel_x being 0"""
        target_data = (5, 10)
        self.assertFalse(sol.is_hit_x(4, 0, target_data))
        self.assertFalse(sol.is_hit_x(11, 0, target_data))

    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_a(_data_small()), 45)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 5995)

    def test_data_o(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_o()), 19503)

    def test_data_t(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_t()), 35511)


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

    def test_data_t(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_t()), 3282)


if __name__ == "__main__":
    unittest.main()
