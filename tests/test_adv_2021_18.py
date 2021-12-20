"""
test for adv_2021_18
"""

import unittest
import general_utils as gu
import solutions.adv_2021_18 as sol


def _data_p():
    return gu.read_input(18, 'p')


def _data_small():
    return gu.read_input(18, 'small')


def _data_very_small():
    return gu.read_input(18, 'very_small')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_get_node(self):
        """test of the function get_node"""
        test_data = (0, ((2, (4, 5)), 6))
        self.assertEqual(sol.get_node(test_data, (0,)), 0)
        self.assertEqual(sol.get_node(test_data, (1, )), ((2, (4, 5)), 6))
        self.assertEqual(sol.get_node(test_data, (1, 0)), (2, (4, 5)))
        self.assertEqual(sol.get_node(test_data, (1, 1)), 6)
        self.assertEqual(sol.get_node(test_data, (1, 0, 0)), 2)
        self.assertEqual(sol.get_node(test_data, (1, 0, 1)), (4, 5))
        self.assertEqual(sol.get_node(test_data, (1, 0, 1, 0)), 4)
        self.assertEqual(sol.get_node(test_data, (1, 0, 1, 1)), 5)

    def test_find_path_do_expl_pair(self):
        """test of the function find_path_expl_pair"""
        test_data = {
            (((((9, 8), 1), 2), 3), 4): (9, 8),
            (7, (6, (5, (4, (3, 2))))): (3, 2),
            ((6, (5, (4, (3, 2)))), 1): (3, 2),
            ((3, (2, (1, (7, 3)))), (6, (5, (4, (3, 2))))): (7, 3),
            ((3, (2, (8, 0))), (9, (5, (4, (3, 2))))): (3, 2)}
        for (cur_arg, true_res) in test_data.items():
            cur_path = sol.find_path_do_expl_pair(cur_arg)
            self.assertEqual(len(cur_path), 4)
            self.assertEqual(sol.get_node(cur_arg, cur_path), true_res)

    def test_find_path_to_first_left(self):
        """test of the function find_path_to_first_left"""
        test_data = {
            (((((9, 8), 1), 2), 3), 4): None,
            (7, (6, (5, (4, (3, 2))))): 4,
            ((6, (5, (4, (3, 2)))), 1): 4,
            ((3, (2, (1, (7, 3)))), (6, (5, (4, (3, 2))))): 1,
            ((3, (2, (8, 0))), (9, (5, (4, (3, 2))))): 4}
        for (cur_arg, true_res) in test_data.items():
            cur_path = sol.find_path_do_expl_pair(cur_arg)
            path_to_first_left = sol.find_path_to_first_left(
                cur_arg, cur_path)
            if path_to_first_left is None:
                self.assertIsNone(true_res)
            else:
                self.assertTrue(path_to_first_left < cur_path)
                self.assertEqual(
                    sol.get_node(cur_arg, path_to_first_left),
                    true_res)

    def test_find_path_to_first_right(self):
        """test of the function find_path_to_first_right"""
        test_data = {
            (((((9, 8), 1), 2), 3), 4): 1,
            (7, (6, (5, (4, (3, 2))))): None,
            ((6, (5, (4, (3, 2)))), 1): 1,
            ((3, (2, (1, (7, 3)))), (6, (5, (4, (3, 2))))): 6,
            ((3, (2, (8, 0))), (9, (5, (4, (3, 2))))): None}
        for (cur_arg, true_res) in test_data.items():
            cur_path = sol.find_path_do_expl_pair(cur_arg)
            path_to_first_right = sol.find_path_to_first_right(
                cur_arg, cur_path)
            if path_to_first_right is None:
                self.assertIsNone(true_res)
            else:
                self.assertTrue(cur_path < path_to_first_right)
                self.assertEqual(
                    sol.get_node(cur_arg, path_to_first_right),
                    true_res)

    def test_find_path_to_expl_pair_2(self):
        """test of the function find_path_to_first_right"""
        self.assertEqual(
            sol.find_path_do_expl_pair(((6, (5, (4, (3, 2)))), 1)),
            (0, 1, 1, 1))

    def test_make_split(self):
        """test of the function make_split"""
        def check_single(in_value, in_true_res):
            self.assertEqual(sol.make_split(in_value), in_true_res)
        test_data = {
            10: (5, 5),
            11: (5, 6),
            12: (6, 6),
            9: 9,
            (3, (4, 3)): (3, (4, 3)),
            ((((0, 7), 4), (15, (0, 13))), (1, 1)):
                ((((0, 7), 4), ((7, 8), (0, 13))), (1, 1)),
            ((((0, 7), 4), ((7, 8), (0, 13))), (1, 1)):
                ((((0, 7), 4), ((7, 8), (0, (6, 7)))), (1, 1))}
        for (cur_val, cur_res) in test_data.items():
            check_single(cur_val, cur_res)

    def test_explode(self):
        """test of the function explode"""
        test_data = {
            ((((0, 7), 4), (7, ((8, 4), 9))), (1, 1)):
                ((((0, 7), 4), (15, (0, 13))), (1, 1)),
            (((((4, 3), 4), 4), (7, ((8, 4), 9))), (1, 1)):
                ((((0, 7), 4), (7, ((8, 4), 9))), (1, 1)),
            ((((0, 7), 4), ((7, 8), (0, (6, 7)))), (1, 1)):
                ((((0, 7), 4), ((7, 8), (6, 0))), (8, 1))}
        for (cur_arg, true_res) in test_data.items():
            self.assertEqual(sol.explode(cur_arg), true_res)

    def test_magnitude(self):
        """test of the function magnitude"""
        test_data = {
            ((1, 2), ((3, 4), 5)): 143,
            ((((0, 7), 4), ((7, 8), (6, 0))), (8, 1)): 1384,
            ((((1, 1), (2, 2)), (3, 3)), (4, 4)): 445,
            ((((3, 0), (5, 3)), (4, 4)), (5, 5)): 791,
            ((((5, 0), (7, 4)), (5, 5)), (6, 6)): 1137,
            ((((8, 7), (7, 7)), ((8, 6), (7, 7))),
             (((0, 7), (6, 6)), (8, 7))): 3488}
        for (cur_arg, cur_val) in test_data.items():
            self.assertEqual(sol.magnitude(cur_arg), cur_val)

    def test_add_all(self):
        """test of the function add_all"""
        test_data = {
            ((1, 1), (2, 2), (3, 3), (4, 4)):
                ((((1, 1), (2, 2)), (3, 3)), (4, 4)),
            ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)):
                ((((3, 0), (5, 3)), (4, 4)), (5, 5)),
            ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)):
                ((((5, 0), (7, 4)), (5, 5)), (6, 6))}
        for (cur_arg, cur_res) in test_data.items():
            self.assertEqual(sol.add_all(cur_arg), cur_res)

    def test_add_all_very_small(self):
        """test of the function add_all againd the example data"""
        sol.add_all(sol.parse_input(_data_very_small()))
        self.assertEqual(
            sol.add_all(sol.parse_input(_data_very_small())),
            ((((8, 7), (7, 7)), ((8, 6), (7, 7))),
             (((0, 7), (6, 6)), (8, 7))))

    def test_data_very_small(self):
        """test agains example data"""
        self.assertEqual(sol.solve_a(_data_very_small()), 3488)

    def test_data_small(self):
        """test agains example data"""
        self.assertEqual(sol.solve_a(_data_small()), 4140)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_p()), 3494)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_small(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_small()), 3993)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_p()), 4712)


if __name__ == '__main__':
    unittest.main()
