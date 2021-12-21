"""
solution of adv_2021_19
"""

import numpy
import functools
import re

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
