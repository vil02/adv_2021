"""
test for adv_2021_23
"""

import unittest
import general_utils as gu
import solutions.adv_2021_23 as sol


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
        self.assertEqual(room_a, ['B', 'A'])
        self.assertEqual(room_b, ['C', 'D'])
        self.assertEqual(room_c, ['B', 'C'])
        self.assertEqual(room_d, ['D', 'A'])

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

#    def test_data_small(self):
#        """test against example data"""
#        self.assertEqual(sol.solve_a(_data_small()), 12521)
#
#    def test_data_p(self):
#        """test against full data"""
#        self.assertEqual(sol.solve_a(_data_p()), 11120)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
#    def test_data_small(self):
#        """test against example data"""
#        self.assertEqual(sol.solve_b(_data_small()), 44169)
#
#    def test_data_p(self):
#        """test against full data"""
#        self.assertEqual(sol.solve_b(_data_p()), 49232)


if __name__ == '__main__':
    unittest.main()
