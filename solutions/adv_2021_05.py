"""
solution of adv_2021_05
"""
import itertools


def _pars_input(in_str):
    def proc_line(in_line):
        def proc_num_str(in_num_str):
            x_str, y_str = in_num_str.split(",")
            return int(x_str), int(y_str)

        start_str, end_str = in_line.split(" -> ")
        x_1, y_1 = proc_num_str(start_str)
        x_2, y_2 = proc_num_str(end_str)
        return x_1, y_1, x_2, y_2

    return [proc_line(_) for _ in in_str.splitlines()]


def all_points_a(x_1, y_1, x_2, y_2):
    """
    returns all of the points on a vertical/horisonal line with ends
    (x_1, y_2), (x_2, y_2)
    """

    def my_range(in_a, in_b):
        return range(min(in_a, in_b), max(in_a, in_b) + 1)

    assert x_1 == x_2 or y_1 == y_2
    return list(itertools.product(my_range(x_1, x_2), my_range(y_1, y_2)))


def all_points_b(x_1, y_1, x_2, y_2):
    """
    returns all of the points on a vertical/horisonal/diagonal line with ends
    (x_1, y_2), (x_2, y_2)
    """

    def sgn(in_val):
        return 1 if in_val >= 1 else -1

    if x_1 == x_2 or y_1 == y_2:
        res = all_points_a(x_1, y_1, x_2, y_2)
    else:
        assert abs(x_2 - x_1) == abs(y_2 - y_1)
        res = []
        if x_2 < x_1:
            x_1, x_2 = x_2, x_1
            y_1, y_2 = y_2, y_1
        res = [
            (cur_x, y_1 + num * sgn(y_2 + 1 - y_1))
            for (num, cur_x) in enumerate(range(x_1, x_2 + 1))
        ]
    return res


def _visit_points(in_data, in_all_points_fun):
    visited_points = {}
    for _ in in_data:
        for cur_point in in_all_points_fun(*_):
            if cur_point in visited_points:
                visited_points[cur_point] += 1
            else:
                visited_points[cur_point] = 1
    return visited_points


def _count_unsafe_points(in_data):
    return sum(1 for _ in in_data.values() if _ > 1)


def solve_a(in_str):
    """solution function for part a"""
    data = _pars_input(in_str)
    data = [
        (x_1, y_1, x_2, y_2)
        for (x_1, y_1, x_2, y_2) in data
        if x_1 == x_2 or y_1 == y_2
    ]
    return _count_unsafe_points(_visit_points(data, all_points_a))


def solve_b(in_str):
    """solution function for part b"""
    return _count_unsafe_points(
        _visit_points(_pars_input(in_str), all_points_b)
    )
