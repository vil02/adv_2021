"""
solution of adv_2021_01
"""


def count_a(in_list):
    """counts the value from part a"""
    res = 0
    for cur_num in range(1, len(in_list)):
        if in_list[cur_num - 1] < in_list[cur_num]:
            res += 1
    return res


def solve_a(in_str):
    """solution function for part a"""
    return count_a([int(_) for _ in in_str.splitlines()])


def count_b(in_list):
    """counts the value from part b"""
    window_size = 3
    assert len(in_list) >= window_size
    sum_list = [sum(in_list[0:window_size])]
    for cur_pos in range(window_size, len(in_list)):
        sum_list.append(
            sum_list[-1] - in_list[cur_pos - window_size] + in_list[cur_pos]
        )
    return count_a(sum_list)


def solve_b(in_str):
    """solution function for part b"""
    return count_b([int(_) for _ in in_str.splitlines()])
