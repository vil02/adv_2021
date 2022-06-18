"""
test for adv_2021_16
"""

import unittest
import general_utils as gu
import solutions.adv_2021_16 as sol


def _data_p():
    return gu.read_input(16, 'p')


def _data_o_1():
    return gu.read_input(16, 'o_1')


def _data_o_2():
    return gu.read_input(16, 'o_2')


def _data_o_3():
    return gu.read_input(16, 'o_3')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_read(self):
        """test of the function read againd the example data"""
        def check_single(in_str, in_true_res, in_true_rem_str):
            res, rem_str = sol.read_data(in_str)
            self.assertEqual(res, in_true_res)
            self.assertEqual(rem_str, in_true_rem_str)
        input_data = {
            '110100101111111000101000':
                ({'version': 6, 'id': 4, 'value': 2021}, '000'),
            '11010001010':
                ({'version': 6, 'id': 4, 'value': 10}, ''),
            '0101001000100100':
                ({'version': 2, 'id': 4, 'value': 20}, ''),
            '1101000101001010010001001000000000':
                ({'version': 6, 'id': 4, 'value': 10},
                 '01010010001001000000000'),
            '00111000000000000110111101000101001010010001001000000000':
                ({'version': 1, 'id': 6,
                  'operator_data':
                      [{'version': 6, 'id': 4, 'value': 10},
                       {'version': 2, 'id': 4, 'value': 20}]}, '0000000'),
            '11101110000000001101010000001100100000100011000001100000':
                ({'version': 7, 'id': 3,
                  'operator_data': [
                      {'version': 2, 'id': 4, 'value': 1},
                      {'version': 4, 'id': 4, 'value': 2},
                      {'version': 1, 'id': 4, 'value': 3}]}, '00000')}

        for (in_str, true_res) in input_data.items():
            check_single(in_str, *true_res)

    def test_example_data(self):
        """test of solve_a againts example data"""
        test_data = {
            '8A004A801A8002F478': 16,
            '620080001611562C8802118E34': 12,
            'C0015000016115A2E0802F182340': 23,
            'A0016C880162017C3686B18A3D4780': 31}
        for (cur_str, cur_res) in test_data.items():
            self.assertEqual(sol.solve_a(cur_str), cur_res)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_p()), 843)

    def test_data_o_1(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_o_1()), 852)

    def test_data_o_2(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_o_2()), 923)

    def test_data_o_3(self):
        """test against full data"""
        self.assertEqual(sol.solve_a(_data_o_3()), 895)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_example_data(self):
        """test of solve_a against example data and some other data"""
        test_data = {
            'C200B40A82': 3,
            '04005AC33890': 54,
            '880086C3E88112': 7,
            'CE00C43D881120': 9,
            'D8005AC2A8F0': 1,
            'F600BC2D8F': 0,
            '9C005AC2F8F0': 0,
            '9C0141080250320F1802104A08': 1,
            '000294200841022044088110220440881102204408811020': 2,
            '3232D42BF9400': 5000000000,
            '32F5DF3B128': 123456789,
            '0600878021220122E1273080': 0,
            '26008C8E2DA0191C5B400': 10000000000,
            '8A004A801A8002F478': 15,
            '02008180210420C4200': 10,
            '0000404E00': 192}
        for (cur_str, cur_res) in test_data.items():
            self.assertEqual(sol.solve_b(cur_str), cur_res)

    def test_data_p(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_p()), 5390807940351)

    def test_data_o_1(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_o_1()), 19348959966392)

    def test_data_o_2(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_o_2()), 258888628940)

    def test_data_o_3(self):
        """test against full data"""
        self.assertEqual(sol.solve_b(_data_o_3()), 1148595959144)


if __name__ == '__main__':
    unittest.main()
