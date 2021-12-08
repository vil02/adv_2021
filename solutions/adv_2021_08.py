"""
solution of adv_2021_08
"""
import itertools


def parse_input_a(in_str):
    """parses input for part a"""
    def proc_single_line(in_line):
        _, part_b = in_line.split(' | ')
        return part_b.split()
    res = []
    for _ in in_str.splitlines():
        res += proc_single_line(_)
    return res


def solve_a(in_str):
    """solution function for part a"""
    data = parse_input_a(in_str)
    return sum(1 for _ in data if len(_) in [2, 4, 3, 7])


def parse_input_b(in_str):
    """parses input for part b"""
    def proc_single_line(in_line):
        part_a, part_b = in_line.split(' | ')
        return part_a.split(), part_b.split()
    return [proc_single_line(_) for _ in in_str.splitlines()]


def solve_single_line(in_part_a, in_part_b):
    """solves single line fro part b"""
    def apply_permutation(in_perm_data, in_str_list):
        def proc_single_str(in_str):
            return ''.join(sorted(in_perm_data[_] for _ in in_str))
        return [proc_single_str(_) for _ in in_str_list]
    d_digits = [
        "abcefg",
        "cf",
        "acdeg",
        "acdfg",
        "bcdf",
        "abdfg",
        "abdefg",
        "acf",
        "abcdefg",
        "abcdfg"]

    def get_value(in_str_list):
        digit_list = [str(d_digits.index(_)) for _ in in_str_list]
        return int(''.join(digit_list))
    all_chars = list(set(''.join(d_digits)))
    d_digits_set = set(d_digits)
    for cur_perm in itertools.permutations(all_chars):
        perm_data = dict(zip(cur_perm, all_chars))
        cur_displays = apply_permutation(perm_data, in_part_a)
        if set(cur_displays) == d_digits_set:
            cur_displays = apply_permutation(perm_data, in_part_b)
            return get_value(cur_displays)


def solve_b(in_str):
    """solution function for part b"""
    return sum(solve_single_line(*_) for _ in parse_input_b(in_str))
