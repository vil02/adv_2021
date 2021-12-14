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


class Rules:
    def __init__(self, in_rules):
        self.rules = in_rules
        self.res_data = {}

    def apply_single(self, in_str):
        if in_str in self.res_data:
            res = self.res_data[in_str]
        else:
            if len(in_str) == 2:
                middle_part = ''
                if in_str in self.rules:
                    middle_part = self.rules[in_str]
                res = in_str[0]+middle_part+in_str[1]
            else:
                assert len(in_str) > 2
                mid_point = len(in_str)//2
                #print(in_str, in_str[:mid_point], in_str[mid_point:])
                part_a = self.apply_single(in_str[:mid_point+1])
                part_b = self.apply_single(in_str[mid_point:])
                res = part_a[:-1]+part_b
            self.res_data[in_str] = res
        return res

def calculate_histogram(in_str):
    res = {}
    for _ in in_str:
        if _ in res:
            res[_] += 1
        else:
            res[_] = 1
    return res

def get_res_val(in_str):
    hist = calculate_histogram(in_str)
    min_val = min(hist.values())
    max_val = max(hist.values())
    return max_val-min_val

def solve_a(in_str):
    """solution function for part a"""
    cur_str, transforms = parse_input(in_str)
    rules_obj = Rules(transforms)
    for _ in range(10):
        cur_str = rules_obj.apply_single(cur_str)
    return get_res_val(cur_str)


def solve_b(in_str):
    """solution function for part b"""
    cur_str, transforms = parse_input(in_str)
    rules_obj = Rules(transforms)
    for _ in range(40):
        cur_str = rules_obj.apply_single(cur_str)
        print(_, len(rules_obj.res_data))
    return get_res_val(cur_str)
