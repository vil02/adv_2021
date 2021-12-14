"""
solution of adv_2021_14
"""
import functools


def parse_input(in_str):
    def proc_single(in_str):
        pattern, result = in_str.split(' -> ')
        assert len(pattern) == 2
        return pattern, result
    lines = in_str.splitlines()
    split_pos = lines.index('')
    start_str = lines[split_pos-1].strip()
    transforms = dict(proc_single(_) for _ in lines[split_pos+1:])
    return start_str, transforms


def calculate_pair_count(in_str):
    res = {}
    for _ in range(len(in_str)-1):
        cur_pair = in_str[_:_+2]
        if cur_pair not in res:
            res[cur_pair] = 0
        res[cur_pair] += 1
    return res


def iterate_pair_count_single(in_pair_count, in_rules):
    res = {}
    for cur_pair in in_pair_count:
        new_char = in_rules[cur_pair]

        if cur_pair[0]+new_char not in res:
            res[cur_pair[0]+new_char] = 0
        res[cur_pair[0]+new_char] += in_pair_count[cur_pair]

        if new_char+cur_pair[1] not in res:
            res[new_char+cur_pair[1]] = 0
        res[new_char+cur_pair[1]] += in_pair_count[cur_pair]
    return res


def pair_count_to_hist(in_pair_count):
    beg_count = {}
    end_count = {}
    for cur_pair in in_pair_count:
        assert len(cur_pair) == 2
        cur_beg = cur_pair[0]
        cur_end = cur_pair[1]
        if cur_beg not in beg_count:
            beg_count[cur_beg] = 0
        beg_count[cur_beg] += in_pair_count[cur_pair]

        if cur_end not in end_count:
            end_count[cur_end] = 0
        end_count[cur_end] += in_pair_count[cur_pair]
    common_key = set(beg_count) | set(end_count)
    return {_: max(beg_count.get(_, 0), end_count.get(_, 0))
            for _ in common_key}

def get_res_val(in_pair_count):
    hist = pair_count_to_hist(in_pair_count)
    return max(hist.values())-min(hist.values())

def solve_a(in_str):
    """solution function for part a"""
    cur_str, transforms = parse_input(in_str)
    pair_count = calculate_pair_count(cur_str)
    for _ in range(10):
        pair_count = iterate_pair_count_single(pair_count, transforms)
    return get_res_val(pair_count)


def solve_b(in_str):
    """solution function for part b"""
    cur_str, transforms = parse_input(in_str)
    pair_count = calculate_pair_count(cur_str)
    for _ in range(40):
        pair_count = iterate_pair_count_single(pair_count, transforms)
    return get_res_val(pair_count)
