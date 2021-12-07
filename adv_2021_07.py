"""
solution of adv_2021_07
"""
import statistics


def parse_input(in_str):
    """returns the list of initial positions"""
    return [int(_) for _ in in_str.split(',')]


def calculate_total_fuel_a(in_position_list, in_target_pos):
    """
    returns the amout of fules needed to align
    in_position_list to in_target_pos
    as described in part_a
    """
    return sum(abs(_-in_target_pos) for _ in in_position_list)


def calculate_total_fuel_b(in_numbers, in_target_pos):
    """
    returns the amout of fules needed to align
    in_position_list to in_target_pos
    as described in part_b
    """
    def cost(in_val):
        return ((in_val+1)*in_val)//2
    return sum(cost(abs(_-in_target_pos)) for _ in in_numbers)


def find_minimal_fuel_usage(in_position_list, in_cost_fun):
    """
    finds the minimal fuel usage in order to aligh all submarines with starting
    positions as in_position_list
    """
    min_val = min(in_position_list)
    max_val = max(in_position_list)
    return min(
        in_cost_fun(in_position_list, _) for _ in range(min_val, max_val+1))


def solve_a(in_str):
    """solution function for part a"""
    position_list = parse_input(in_str)
    return calculate_total_fuel_a(
        position_list, statistics.median(position_list))


def solve_b(in_str):
    """solution function for part b"""
    return find_minimal_fuel_usage(parse_input(in_str), calculate_total_fuel_b)
