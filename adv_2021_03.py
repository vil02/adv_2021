"""
solution of adv_2021_template
"""


def count_most_common(in_str_list, in_pos):
    number_of_ones = sum(1 for _ in in_str_list if _[in_pos] == '1')
    res = '1'
    if 2*number_of_ones <= len(in_str_list):
        res = '0'
    return res, number_of_ones


def solve_a(in_str):
    """solution function for part a"""
    def flip(in_char):
        res = '0'
        if in_char == '0':
            res = '1'
        return res
    str_list = in_str.split()
    gamma_bits = [count_most_common(str_list, _)[0] for _ in range(len(str_list[0]))]
    gamma = int(''.join(gamma_bits), 2)
    other_bits = [flip(_) for _ in gamma_bits]
    other = int(''.join(other_bits), 2)
    return gamma*other


def get_oxygen(in_str_list):
    cur_pos = 0
    cur_str_list = [_ for _ in in_str_list]
    while True:
        most_common, count = count_most_common(cur_str_list, cur_pos)
        if 2*count == len(cur_str_list):
            most_common = '1'
        cur_str_list = [_ for _ in cur_str_list if _[cur_pos] == most_common]
        if len(cur_str_list) == 1:
            return int(cur_str_list[0], 2)
        else:
            cur_pos += 1


def get_co2(in_str_list):
    cur_pos = 0
    cur_str_list = [_ for _ in in_str_list]
    while True:
        most_common, count = count_most_common(cur_str_list, cur_pos)
        if 2*count == len(cur_str_list):
            most_common = '1'
        cur_str_list = [_ for _ in cur_str_list if _[cur_pos] != most_common]
        if len(cur_str_list) == 1:
            return int(cur_str_list[0], 2)
        else:
            cur_pos += 1


def solve_b(in_str):
    """solution function for part b"""
    str_list = in_str.split()
    return get_oxygen(str_list)*get_co2(str_list)
