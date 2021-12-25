"""
test for adv_2021_23
"""

import unittest
import general_utils as gu
import solutions.adv_2021_23 as sol

import sys
sys.setrecursionlimit(2300)

def _data_small():
    return gu.read_input(23, 'small')


def _data_p():
    return gu.read_input(23, 'p')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_parse_input(self):
        """test function parse_input against example data"""
        room_a, room_b, room_c, room_d = sol.parse_input(_data_small())
        self.assertEqual(room_a, ('B', 'A'))
        self.assertEqual(room_b, ('C', 'D'))
        self.assertEqual(room_c, ('B', 'C'))
        self.assertEqual(room_d, ('D', 'A'))

    def test_calculate_move_length(self):
        """test of calculate_move_length"""
        test_data = {
            ('A', 0, 0): 3,
            ('B', 2, 5): 4,
            ('C', 3, 0): 10}
        for (cur_arg, true_res) in test_data.items():
            self.assertEqual(sol.calculate_move_length(*cur_arg), true_res)

    def test_is_move_possible_postive(self):
        """positive tests of is_move_possible"""
        test_corridor = ['' for _ in range(11)]
        test_corridor[0] = 'X'
        test_corridor[9] = 'X'
        test_corridor[5] = 'X'
        test_corridor = tuple(test_corridor)
        test_data = [
            ('A', 1), ('A', 3),
            ('B', 1), ('B', 3),
            ('C', 7),
            ('D', 7)]
        for _ in test_data:
            self.assertTrue(sol.is_move_possible(*_, test_corridor))

    def test_is_move_possible_negative(self):
        """negatve tests of is_move_possible"""
        test_corridor = ['' for _ in range(11)]
        test_corridor[0] = 'X'
        test_corridor[9] = 'X'
        test_corridor[5] = 'X'
        test_corridor = tuple(test_corridor)
        test_data = [
            ('A', 7), ('A', 10), ('A', 0),
            ('B', 0), ('B', 7), ('B', 9), ('B', 10),
            ('C', 0), ('C', 1), ('C', 3), ('C', 9), ('C', 10),
            ('D', 0), ('D', 1), ('D', 3), ('D', 5), ('D', 10)]
        for _ in test_data:
            self.assertFalse(sol.is_move_possible(*_, test_corridor))

    def test_find_min_cost_trivial_input(self):
        solved_rooms = (
                ('A', 'A', 'A', 'A'),
                ('B', 'B', 'B', 'B'),
                ('C', 'C', 'C', 'C'),
                ('D', 'D', 'D', 'D'))
        self.assertEqual(sol.find_min_cost(solved_rooms), 0)

    def test_is_room_done_positive(self):
        test_data = [
            (0, ('A', 'A')),
            (0, ('A', 'A', 'A', 'A')),
            (1, ('B', 'B')),
            (3, ('D', 'D'))]
        for _ in test_data:
            self.assertTrue(sol.is_room_done(*_))

    def test_is_room_done_negative(self):
        test_data = [
            (0, ('', 'A')),
            (0, ('A', 'B')),
            (0, ('', '')),
            (0, ('A', 'B', 'A', 'A')),
            (1, ('B', 'D')),
            (3, ('C', 'A'))]
        for _ in test_data:
            self.assertFalse(sol.is_room_done(*_))

    def test_can_go_home_positive(self):
        test_rooms = (
            ('', 'A'),
            ('', 'B'),
            ('', 'C'),
            ('', 'D'))
        test_corridor = ('A', '', '', 'B', '', '', '', 'C', '', '', 'D')
        self.assertTrue(sol.can_go_home('A', 0, test_corridor, test_rooms))
        self.assertTrue(sol.can_go_home('B', 3, test_corridor, test_rooms))
        self.assertTrue(sol.can_go_home('C', 7, test_corridor, test_rooms))
        self.assertTrue(sol.can_go_home('D', 10, test_corridor, test_rooms))

    def test_is_room_almost_done_positive(self):
        test_rooms = (
            ('', '', '', 'A'),
            ('', '', 'B', 'B'),
            ('', 'C', 'C', 'C'),
            ('', '', '', ''),)
        for _ in range(4):
            self.assertTrue(sol.is_room_almost_done(_, test_rooms))

    def test_is_room_almost_done_negative(self):
        test_rooms = (
            ('', '', '', 'B'),
            ('', '', 'A', 'B'),
            ('C', 'C', 'C', 'C'),
            ('', '', '', 'A'),)
        for _ in range(4):
            self.assertFalse(sol.is_room_almost_done(_, test_rooms))

    def test_is_starting_room_positive(self):
        test_rooms = (('A', 'B'), ('', 'C'), ('B', 'C'), ('D', 'A'))
        for _ in range(4):
            self.assertTrue(sol.is_starting_room(_, test_rooms))

    def test_is_starting_room_negative(self):
        test_rooms = (('', 'A'), ('B', 'B'), ('', ''), ('', 'D'))
        for _ in range(4):
            self.assertFalse(sol.is_starting_room(_, test_rooms))

    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_a(_data_small()), 12521)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 11120)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_extend_data(self):
        room_a, room_b, room_c, room_d = sol.extend_data(
            sol.parse_input(_data_small()))
        self.assertEqual(room_a, ('B', 'D', 'D', 'A'))
        self.assertEqual(room_b, ('C', 'C', 'B', 'D'))
        self.assertEqual(room_c, ('B', 'B', 'A', 'C'))
        self.assertEqual(room_d, ('D', 'A', 'C', 'A'))

    def test_data_small(self):
        """test against example data"""
        self.assertEqual(sol.solve_b(_data_small()), 44169)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 49232)


if __name__ == '__main__':
    unittest.main()
