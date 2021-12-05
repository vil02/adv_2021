"""
solution of adv_2021_template
"""
import itertools


def _pars_input(in_str):
    def proc_line(in_line):
        def proc_num_str(in_num_str):
            x_str, y_str = in_num_str.split(',')
            return int(x_str), int(y_str)
        start_str, end_str = in_line.split(' -> ')
        x_1, y_1 = proc_num_str(start_str)
        x_2, y_2 = proc_num_str(end_str)
        return x_1, y_1, x_2, y_2
    return [proc_line(_) for _ in in_str.splitlines()]


def all_points_a(x_1, y_1, x_2, y_2):
    def my_range(a, b):
        if a < b:
            res = range(a, b+1)
        else:
            res = range(b, a+1)
        return res
    assert x_1 == x_2 or y_1 == y_2
    res = list(itertools.product(my_range(x_1, x_2), my_range(y_1, y_2)))
    # print(x_1, y_1, x_2, y_2, res)
    return res


def all_points_b(x_1, y_1, x_2, y_2):
    def sgn(in_val):
        return 1 if in_val >= 1 else -1
    if x_1 == x_2 or y_1 == y_2:
        res = all_points_a(x_1, y_1, x_2, y_2)
    else:
        assert abs(x_2-x_1) == abs(y_2-y_1)
        res = []
        if x_2 < x_1:
            x_1, x_2 = x_2, x_1
            y_1, y_2 = y_2, y_1
        for (num, cur_x) in enumerate(range(x_1, x_2+1)):
            res.append((cur_x, y_1+num*sgn(y_2+1-y_1)))
    return res



def solve_a(in_str):
    """solution function for part a"""
    data = _pars_input(in_str)
    data = [(x_1, y_1, x_2, y_2)
            for (x_1, y_1, x_2, y_2) in data if x_1 == x_2 or y_1 == y_2]
    visited_points = {}
    for _ in data:
        new_points = all_points_a(*_)
        for cur_point in new_points:
            if cur_point in visited_points:
                visited_points[cur_point] += 1
            else:
                visited_points[cur_point] = 1
    return sum(1 for val in visited_points.values() if val > 1)


def solve_b(in_str):
    """solution function for part b"""
    data = _pars_input(in_str)
    visited_points = {}
    for _ in data:
        new_points = all_points_b(*_)
        for cur_point in new_points:
            if cur_point in visited_points:
                visited_points[cur_point] += 1
            else:
                visited_points[cur_point] = 1
    return sum(1 for val in visited_points.values() if val > 1)
