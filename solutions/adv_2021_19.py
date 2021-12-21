"""
solution of adv_2021_19
"""

import numpy
import functools
import heapq

@functools.lru_cache(1)
def get_all_rotations_3d():
    """returns matrices of all 90-degree trotations in 3d"""
    id_mat = numpy.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]])
    x_rot = numpy.array([
        [1, 0, 0],
        [0, 0, -1],
        [0, 1, 0]])
    y_rot = numpy.array([
        [0, 0, 1],
        [0, 1, 0],
        [-1, 0, 0]])
    return [
        id_mat,
        x_rot,
        y_rot,
        x_rot@x_rot,
        x_rot@y_rot,
        y_rot@x_rot,
        y_rot@y_rot,
        x_rot@x_rot@x_rot,
        x_rot@x_rot@y_rot,
        x_rot@y_rot@x_rot,
        x_rot@y_rot@y_rot,
        y_rot@x_rot@x_rot,
        y_rot@y_rot@x_rot,
        y_rot@y_rot@y_rot,
        x_rot@x_rot@x_rot@y_rot,
        x_rot@x_rot@y_rot@x_rot,
        x_rot@x_rot@y_rot@y_rot,
        x_rot@y_rot@x_rot@x_rot,
        x_rot@y_rot@y_rot@y_rot,
        y_rot@x_rot@x_rot@x_rot,
        y_rot@y_rot@y_rot@x_rot,
        x_rot@x_rot@x_rot@y_rot@x_rot,
        x_rot@y_rot@x_rot@x_rot@x_rot,
        x_rot@y_rot@y_rot@y_rot@x_rot]


def parse_input(in_str):
    """
    returns a list of measurments from each scanner
    """
    res_list = []
    for cur_line in in_str.splitlines():
        if 'scanner' in cur_line:
            scanner_data = []
        elif not cur_line:
            res_list.append(scanner_data)
        else:
            cur_row = [int(_) for _ in cur_line.split(',')]
            scanner_data.append(numpy.array(cur_row))
            assert scanner_data[-1].shape == (3,)
            assert scanner_data[-1].size == 3
    return res_list


def extract_x(in_data):
    """returns the list of x-coordinates from the vectors stored in in_data"""
    return [_[0] for _ in in_data]


def extract_xy(in_data):
    """
    returns the list of xy-coordinates from the vectors stored in in_data
    """
    return [numpy.array(_[0:2]) for _ in in_data]


def _get_suitable_shifts(
        in_merged_data, in_scanner_data,
        in_extract_fun, in_shift_fun,
        in_proc_data_fun,
        shift_range):
    def get_shifted(in_data, in_shift):
        return {in_shift_fun(_, in_shift) for _ in in_data}

    def prepare_data(in_data):
        return {in_proc_data_fun(_) for _ in in_extract_fun(in_data)}
    merged_proj_data = prepare_data(in_merged_data)
    scanner_proj_data = prepare_data(in_scanner_data)
    raw_res = []
    initial_size = len(merged_proj_data | scanner_proj_data)
    raw_res = []
    for _ in shift_range:
        cur_size = len(merged_proj_data | get_shifted(scanner_proj_data, _))
        if cur_size < initial_size:
            heapq.heappush(raw_res, (cur_size, _))
    return [_[1] for _ in raw_res]


def get_suitable_x_shifts(in_merged_data, in_scanner_data, x_range):
    return _get_suitable_shifts(
        in_merged_data, in_scanner_data,
        extract_x, lambda x, s: x+s,
        lambda x: x,
        x_range)


def get_suitable_y_shifts(in_merged_data, in_scanner_data, y_range):
    return _get_suitable_shifts(
        in_merged_data, in_scanner_data,
        extract_xy, lambda xy, s: (xy[0], xy[1]+s),
        lambda x: tuple(x),
        y_range)


def get_suitable_z_shifts(in_merged_data, in_scanner_data, z_range):
    return _get_suitable_shifts(
        in_merged_data, in_scanner_data,
        lambda x: x,
        lambda xyz, s: (xyz[0], xyz[1], xyz[2]+s),
        lambda x: tuple(x),
        z_range)


def merge_single(in_merged_data, in_scanner_data):
    pass


def merge_data(in_scanner_data_list):
    pass


# def solve_a(in_str):
#     """solution function for part a"""
#     pass


# def solve_b(in_str):
#     """solution function for part b"""
#     pass
