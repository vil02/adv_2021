"""
solution of adv_2021_19
"""

import functools
import itertools
import collections
import copy
import numpy


@functools.lru_cache(1)
def get_all_rotations_3d():
    """returns matrices of all 90-degree trotations in 3d"""
    id_mat = numpy.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    x_rot = numpy.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
    y_rot = numpy.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
    return [
        id_mat,
        x_rot,
        y_rot,
        x_rot @ x_rot,
        x_rot @ y_rot,
        y_rot @ x_rot,
        y_rot @ y_rot,
        x_rot @ x_rot @ x_rot,
        x_rot @ x_rot @ y_rot,
        x_rot @ y_rot @ x_rot,
        x_rot @ y_rot @ y_rot,
        y_rot @ x_rot @ x_rot,
        y_rot @ y_rot @ x_rot,
        y_rot @ y_rot @ y_rot,
        x_rot @ x_rot @ x_rot @ y_rot,
        x_rot @ x_rot @ y_rot @ x_rot,
        x_rot @ x_rot @ y_rot @ y_rot,
        x_rot @ y_rot @ x_rot @ x_rot,
        x_rot @ y_rot @ y_rot @ y_rot,
        y_rot @ x_rot @ x_rot @ x_rot,
        y_rot @ y_rot @ y_rot @ x_rot,
        x_rot @ x_rot @ x_rot @ y_rot @ x_rot,
        x_rot @ y_rot @ x_rot @ x_rot @ x_rot,
        x_rot @ y_rot @ y_rot @ y_rot @ x_rot,
    ]


def parse_input(in_str):
    """returns a list of measurments from each scanner"""
    res_list = []

    def append_result(in_scanner_data):
        res_list.append(tuple(in_scanner_data))

    for cur_line in in_str.splitlines():
        if "scanner" in cur_line:
            scanner_data = []
        elif not cur_line:
            append_result(scanner_data)
            scanner_data = []
        else:
            cur_row = tuple(int(_) for _ in cur_line.split(","))
            scanner_data.append(tuple(cur_row))
            assert len(scanner_data[-1]) == 3
    append_result(scanner_data)
    return tuple(res_list)


def shift_data(in_data, in_shift):
    """returns in_data shifted by the vector in_shift"""

    def proc_single_vec(in_vec):
        return tuple(v + s for (v, s) in zip(in_vec, in_shift))

    return tuple(proc_single_vec(_) for _ in in_data)


def rotate_data(in_rotation, in_data):
    """returns in_data rotated by in_rotation"""

    def proc_vec(in_vec):
        return tuple(int(_) for _ in in_vec)

    tmp_data = in_rotation @ numpy.array(in_data).transpose()
    return tuple(proc_vec(_) for _ in tmp_data.transpose())


def transform_data(in_rotation, in_data, in_shift):
    """
    returns in_data rotated by in_rotation and shifted by the vector in_shift
    """
    return shift_data(rotate_data(in_rotation, in_data), in_shift)


def minus(in_vec_a, in_vec_b):
    """
    returns the vector in_vec_a - in_vec_b
    """
    return tuple(a - b for (a, b) in zip(in_vec_a, in_vec_b))


def get_shift_dict(in_merged_data, in_scanner_data):
    """
    returns the histogram of differences between the points
    in in_merged_data and in_scanner_data
    """
    return collections.Counter(
        minus(a, b) for (a, b) in itertools.product(in_merged_data, in_scanner_data)
    )


def merge_single(in_merged_data, in_scanner_data, in_rotation, in_shift):
    """
    merges the in_merged_data with suitably transformed in_scanner_data
    """
    tmp_data = transform_data(in_rotation, in_scanner_data, in_shift)
    return in_merged_data | set(tmp_data)


@functools.lru_cache(None)
def calculate_result(in_all_data):
    """
    returns merged data from all of the scanners and their psotion list
    """
    merged_data = set(in_all_data[0])
    scanner_data = list(copy.deepcopy(in_all_data[1:]))
    scanner_pos_list = [(0, 0, 0)]
    while scanner_data:
        cur_scanner_data = scanner_data.pop(0)
        was_fit = False
        for cur_rot in get_all_rotations_3d():
            shift_dict = get_shift_dict(
                merged_data, rotate_data(cur_rot, cur_scanner_data)
            )
            if max(shift_dict.values()) >= 8:
                best_shift = max(shift_dict, key=shift_dict.get)
                merged_data = merge_single(
                    merged_data, cur_scanner_data, cur_rot, best_shift
                )
                scanner_pos_list.append(best_shift)
                was_fit = True
                break
        if not was_fit:
            scanner_data.append(cur_scanner_data)
    return merged_data, scanner_pos_list


def solve_a(in_str):
    """solution function for part a"""
    merged_data, _ = calculate_result(parse_input(in_str))
    return len(merged_data)


def find_max_dist(in_list):
    """
    returns the maximum Manhattan distance between the vectors in the in_list
    """

    def m_dist(in_vec_a, in_vec_b):
        return sum(abs(_) for _ in minus(in_vec_a, in_vec_b))

    return max(m_dist(*_) for _ in itertools.combinations(in_list, 2))


def solve_b(in_str):
    """solution function for part b"""
    _, scanner_pos_list = calculate_result(parse_input(in_str))
    return find_max_dist(scanner_pos_list)
