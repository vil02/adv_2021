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
        self.assertEqual(len(res), 4)
        for _ in res:
            self.assertTrue(_)

    def test_extract_x(self):
        """test of the function extract_x"""
        test_data = [
            numpy.array([1, 2, 3]),
            numpy.array([10, 20, 30]),
            numpy.array([100, 200, 300])]
        res_data = sol.extract_x(test_data)
        self.assertEqual(res_data, [1, 10, 100])

    def test_extract_xy(self):
        """test of the function extract_xy"""
        test_data = [
            numpy.array([1, 2, 3]),
            numpy.array([10, 20, 30]),
            numpy.array([100, 200, 300])]
        true_res = [
                numpy.array([1, 2]),
                numpy.array([10, 20]),
                numpy.array([100, 200])]
        res_data = sol.extract_xy(test_data)
        for (a, b) in zip(res_data, true_res):
            self.assertTrue(numpy.array_equal(a, b))

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
