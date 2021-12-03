"""
solution of adv_2021_template
"""


def _count_ones(in_str_list, in_pos):
    return sum(1 for _ in in_str_list if _[in_pos] == '1')


def _find_most_common(in_str_list, in_pos):
    one_count = _count_ones(in_str_list, in_pos)
    return '1' if 2*one_count >= len(in_str_list) else '0'


def calculate_gamma(in_str_list):
    """returns the value of gamma rate"""
    def get_bit(in_pos):
        return _find_most_common(in_str_list, in_pos)
    assert len({len(_) for _ in in_str_list}) == 1
    res_bits = ''.join(get_bit(_) for _ in range(len(in_str_list[0])))
    return int(res_bits, 2)


def calculate_epsilon(in_str_list):
    """returns the value of epsilon rate"""
    gamma_val = calculate_gamma(in_str_list)
    assert gamma_val >= 0
    gamma_bin_str = bin(gamma_val)
    assert gamma_bin_str.startswith('0b')
    gamma_bin_str = gamma_bin_str[2:]
    flip_dict = {'0': '1', '1': '0'}
    return int(''.join(flip_dict[_] for _ in gamma_bin_str), 2)


def solve_a(in_str):
    """solution function for part a"""
    str_list = in_str.split()
    return calculate_gamma(str_list)*calculate_epsilon(str_list)


def calculate_oxygen(in_str_list):
    """returns the oxygen generator rating from part b"""
    cur_pos = 0
    cur_str_list = [_ for _ in in_str_list]
    while True:
        most_common = _find_most_common(cur_str_list, cur_pos)
        cur_str_list = [_ for _ in cur_str_list if _[cur_pos] == most_common]
        if len(cur_str_list) == 1:
            return int(cur_str_list[0], 2)
        else:
            cur_pos += 1


def calculate_c02(in_str_list):
    """returns the CO2 scrubber rating from part b"""
    cur_pos = 0
    cur_str_list = [_ for _ in in_str_list]
    while True:
        most_common = _find_most_common(cur_str_list, cur_pos)
        cur_str_list = [_ for _ in cur_str_list if _[cur_pos] != most_common]
        if len(cur_str_list) == 1:
            return int(cur_str_list[0], 2)
        else:
            cur_pos += 1


def solve_b(in_str):
    """solution function for part b"""
    str_list = in_str.split()
    return calculate_oxygen(str_list)*calculate_c02(str_list)
