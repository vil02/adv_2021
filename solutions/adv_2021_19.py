"""
solution of adv_2021_19
"""

import numpy


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
        [-1, 0, 1]])
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
        x_rot@y_rot@x_rot@y_rot@x_rot]


get_all_rotations_3d()

# def solve_a(in_str):
#     """solution function for part a"""
#     pass


# def solve_b(in_str):
#     """solution function for part b"""
#     pass
