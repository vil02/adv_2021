"""
test for adv_2021_19
"""

import unittest
import itertools
import numpy
import general_utils as gu
import solutions.adv_2021_19 as sol


def _data_small():
    return gu.read_input(19, 'small')


def _data_p():
    return gu.read_input(19, 'p')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_get_all_rotations_3d(self):
        """
        test of the function get_all_rotations_3d
        """
        rotations = sol.get_all_rotations_3d()
        for _ in rotations:
            self.assertEqual(numpy.linalg.det(_), 1)
            self.assertTrue(numpy.array_equal(
                numpy.linalg.inv(_), numpy.transpose(_)))
        self.assertEqual(len(rotations), 24)
        self.assertEqual(len({tuple(_.flat) for _ in rotations}), 24)
        for _ in itertools.product(rotations, repeat=2):
            self.assertTrue(any(
                numpy.array_equal(_[0]@_[1], cur_rot)
                for cur_rot in rotations))

    def test_parse_input(self):
        """tests the function parse_input against example data"""
        res = sol.parse_input(_data_small())
        self.assertEqual(len(res), 5)
        for _ in res:
            self.assertTrue(_)
            self.assertIn(len(_), {25, 26})
        self.assertEqual(res[0][0], (404, -588, -901))
        self.assertEqual(res[0][-1], (459, -707, 401))
        self.assertEqual(res[1][0], (686, 422, 578))
        self.assertEqual(res[1][-1], (553, 889, -390))
        self.assertEqual(res[-1][0], (727, 592, 562))
        self.assertEqual(res[-1][-1], (30, -46, -14))

    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_a(_data_small()), 79)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 338)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_b(_data_small()), 3621)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 9862)


if __name__ == '__main__':
    unittest.main()
