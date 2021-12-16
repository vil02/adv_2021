"""
test for adv_2021_16
"""

import unittest
import general_utils as gu
import solutions.adv_2021_16 as sol


def _data_small():
    return gu.read_input(16, 'small')


def _data_p():
    return gu.read_input(16, 'p')


class TestSolutionA(unittest.TestCase):
    """
    unit tests for part a
    """
    def test_read_data_0(self):
        res, rem_str = sol.read_data('110100101111111000101000')
        self.assertEqual(res['version'], 6)
        self.assertEqual(res['id'], 4)
        self.assertEqual(res['value'], 2021)
        #self.assertEqual(rem_str, '')

    def test_read_data_1(self):
        res, rem_str = sol.read_data('11010001010')
        self.assertEqual(res['version'], 6)
        self.assertEqual(res['id'], 4)
        self.assertEqual(res['value'], 10)
        #self.assertFalse(rem_str)

    def test_read_data_2(self):
        res, rem_str = sol.read_data('0101001000100100')
        self.assertEqual(res['version'], 2)
        self.assertEqual(res['id'], 4)
        self.assertEqual(res['value'], 20)
        #self.assertFalse(rem_str)

    # def test_read_3(self):
    #     res, rem_str = sol.read_data('110100010100')
    #     self.assertEqual(res['version'], 6)
    #     self.assertEqual(res['id'], 4)
    #     self.assertEqual(res['value'], 10)
    #     self.assertFalse(rem_str)
    #
    # def test_read_4(self):
    #     res, rem_str = sol.read_data('1101000101001')
    #     self.assertEqual(res['version'], 6)
    #     self.assertEqual(res['id'], 4)
    #     self.assertEqual(res['value'], 10)
    #     self.assertEqual(rem_str, '1')
    #
    # def test_read_5(self):
    #     res, rem_str = sol.read_data('1101000101000')
    #     self.assertEqual(res['version'], 6)
    #     self.assertEqual(res['id'], 4)
    #     self.assertEqual(res['value'], 10)
    #     self.assertEqual(rem_str, '0')
    #
    # def test_read_6(self):
    #     res, rem_str = sol.read_data('11010001010001')
    #     self.assertEqual(res['version'], 6)
    #     self.assertEqual(res['id'], 4)
    #     self.assertEqual(res['value'], 10)
    #     self.assertEqual(rem_str, '01')


    def test_read_7(self):
        res, rem_str = sol.read_data('1101000101001010010001001000000000')
        self.assertEqual(res['version'], 6)
        self.assertEqual(res['id'], 4)
        self.assertEqual(res['value'], 10)
        self.assertEqual(rem_str, '01010010001001000000000')

    def test_read_data_8(self):
        res, rem_str = sol.read_data('00111000000000000110111101000101001010010001001000000000')
        self.assertEqual(res['version'], 1)
        self.assertEqual(res['id'], 6)
        self.assertEqual(len(res['operator_data']), 2)
        self.assertEqual(res['operator_data'][0]['value'], 10)
        self.assertEqual(res['operator_data'][1]['value'], 20)
        self.assertEqual(rem_str, '0000000')

    def test_read_data_9(self):
        res, rem_str = sol.read_data('11101110000000001101010000001100100000100011000001100000')
        true_res = {
            'version': 7,
            'id': 3,
            'operator_data': [
                {'version': 2, 'id': 4, 'value': 1},
                {'version': 4, 'id': 4, 'value': 2},
                {'version': 1, 'id': 4, 'value': 3}]}
        self.assertEqual(res, true_res)
        self.assertEqual(rem_str, '00000')

    def test_example_data(self):
        self.assertEqual(sol.solve_a('8A004A801A8002F478'), 16)
        self.assertEqual(sol.solve_a('620080001611562C8802118E34'), 12)
        self.assertEqual(sol.solve_a('C0015000016115A2E0802F182340'), 23)
        self.assertEqual(sol.solve_a('A0016C880162017C3686B18A3D4780'), 31)

    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_a(_data_p()), 843)


class TestSolutionB(unittest.TestCase):
    """
    unit tests for part b
    """
    def test_data_p(self):
        """test agains full data"""
        self.assertEqual(sol.solve_b(_data_p()), 5390807940351)


if __name__ == '__main__':
    unittest.main()
