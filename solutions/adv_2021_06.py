"""
solution of adv_2021_06
"""

import functools


def parse_input(in_str):
    """parses the input"""
    return [int(_) for _ in in_str.split(",")]


@functools.lru_cache(None)
def simulate_fish(in_value, in_days):
    """
    returns the number of fish produced by a fish with
    inner counter starting at in_value after in_days
    """
    if in_value == 0 and in_days > 0:
        res = simulate_fish(8, in_days - 1) + simulate_fish(6, in_days - 1)
    elif in_value == 0 or in_days == 0:
        res = 1
    else:
        res = simulate_fish(in_value - 1, in_days - 1)
    return res


def count_number_of_all_fish(in_value_list, in_days):
    """returns the total number of fish after in_days"""
    return sum(simulate_fish(_, in_days) for _ in in_value_list)


def solve_a(in_str):
    """solution function for part a"""
    return count_number_of_all_fish(parse_input(in_str), 80)


def solve_b(in_str):
    """solution function for part b"""
    return count_number_of_all_fish(parse_input(in_str), 256)
