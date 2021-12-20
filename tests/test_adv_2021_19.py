"""
test for adv_2021_19
"""

import unittest
import general_utils as gu
import solutions.adv_2021_19 as sol
import numpy


def _data_p():
    return gu.read_input(19, 'p')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_get_all_rotations_3d(self):
        rotations = sol.get_all_rotations_3d()
        for _ in rotations:
            self.assertEqual(numpy.linalg.det(_), 1)
        self.assertEqual(len(rotations), 24)
        self.assertEqual(len(set([tuple(_.flat) for _ in rotations])), 24)

    # def test_data_p(self):
    #     """test agains full data"""
    #     self.assertEqual(sol.solve_a(_data_p()), -1)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    # def test_data_p(self):
    #     """test agains full data"""
    #     self.assertEqual(sol.solve_b(_data_p()), -1)


if __name__ == '__main__':
    unittest.main()
