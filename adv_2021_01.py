"""
solution of adv_2021_01
"""


def count_a(in_list):
    """counts the value from part a"""
    res = 0
    for cur_num in range(1, len(in_list)):
        if in_list[cur_num-1] < in_list[cur_num]:
            res += 1
    return res


def solve_a(in_str):
    """solution function for part a"""
    return count_a([int(_) for _ in in_str.splitlines()])


def count_b(in_list):
    """counts the value from part b"""
    sum_list = [sum(in_list[0:3])]
    for cur_pos in range(3, len(in_list)):
        sum_list.append(sum_list[-1]-in_list[cur_pos-3]+in_list[cur_pos])
    return count_a(sum_list)


def solve_b(in_str):
    """solution function for part b"""
    return count_b([int(_) for _ in in_str.splitlines()])
