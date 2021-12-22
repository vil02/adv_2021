"""
solution of adv_2021_22
"""
import itertools
import functools


def parse_input_a(in_str):
    """parses input for the part a"""
    def proc_line(in_line_str):
        def proc_single_piece(in_piece_str):
            assert in_piece_str[1] == '='
            num_str_list = in_piece_str[2:].split('..')
            assert len(num_str_list) == 2
            return tuple(int(_) for _ in num_str_list)
        new_state, num_data_str = in_line_str.split(' ')
        range_data = tuple(
            proc_single_piece(_) for _ in num_data_str.split(','))
        return new_state, range_data
    return [proc_line(_) for _ in in_str.splitlines()]


def simulate_a(in_data):
    """returns the set of active cubes"""
    def my_range(in_min, in_max):
        return range(max(in_min, -50), min(in_max, 50)+1)

    def get_range(in_range_data):
        return itertools.product(*[my_range(*_) for _ in in_range_data])

    cubes_on = set()
    for (cur_state, cur_range) in in_data:
        fun_dict = {
            'on': lambda elem, data_set=cubes_on: data_set.add(elem),
            'off': lambda elem, data_set=cubes_on: data_set.discard(elem)}
        for _ in get_range(cur_range):
            fun_dict[cur_state](_)
    return cubes_on


def solve_a(in_str):
    """solution function for part a"""
    return len(simulate_a(parse_input_a(in_str)))


def parse_input_b(in_str):
    """parses input for the part b"""
    def proc_single(in_row):
        def proc_range_data(in_range_data):
            return in_range_data[0], in_range_data[1]+1
        state = in_row[0]
        all_range_data = tuple(proc_range_data(_) for _ in in_row[1])
        return state, all_range_data
    return [proc_single(_) for _ in parse_input_a(in_str)]


def _get_unique_coordinates(in_all_data, in_axis_num):
    res = set()
    for _, all_range_data in in_all_data:
        range_data = all_range_data[in_axis_num]
        assert len(range_data) == 2
        res.add(range_data[0])
        res.add(range_data[1])
    return sorted(res)


def _get_coordinate_dict(in_uniqe_coordinates):
    return {val: num for num, val in enumerate(in_uniqe_coordinates)}


def _get_grid_cell_volume(
        in_all_uniuqe_coordinates, in_coord_num_list):
    def get_size(in_axis):
        cur_coords = in_all_uniuqe_coordinates[in_axis]
        return cur_coords[in_coord_num_list[in_axis]+1] \
            - cur_coords[in_coord_num_list[in_axis]]
    assert len(in_all_uniuqe_coordinates) == len(in_coord_num_list)
    return functools.reduce(
        lambda a, b: a*b,
        (get_size(_) for _ in range(len(in_coord_num_list))))


def _get_grid(in_all_uniuqe_coordinates):
    x_grid_size = len(in_all_uniuqe_coordinates[0])-1
    y_grid_size = len(in_all_uniuqe_coordinates[1])-1
    z_grid_size = len(in_all_uniuqe_coordinates[2])-1
    return [[[False] * z_grid_size for _ in range(y_grid_size)]
            for _ in range(x_grid_size)]


def _simulate_on_grid(in_all_data):
    all_uniuqe_coordinates = [
        _get_unique_coordinates(in_all_data, _) for _ in range(3)]
    grid = _get_grid(all_uniuqe_coordinates)
    x_dict = _get_coordinate_dict(all_uniuqe_coordinates[0])
    y_dict = _get_coordinate_dict(all_uniuqe_coordinates[1])
    z_dict = _get_coordinate_dict(all_uniuqe_coordinates[2])
    for (state_str, data) in in_all_data:
        for _ in itertools.product(
                range(x_dict[data[0][0]], x_dict[data[0][1]]),
                range(y_dict[data[1][0]], y_dict[data[1][1]]),
                range(z_dict[data[2][0]], z_dict[data[2][1]])):
            grid[_[0]][_[1]][_[2]] = state_str == 'on'
    return all_uniuqe_coordinates, grid


def solve_b(in_str):
    """solution function for part b"""
    all_data = parse_input_b(in_str)

    all_uniuqe_coordinates, grid = _simulate_on_grid(all_data)

    volume = 0
    for (x_num, grid_data_x) in enumerate(grid):
        for (y_num, grid_data_y) in enumerate(grid_data_x):
            for (z_num, grid_state) in enumerate(grid_data_y):
                if grid_state:
                    volume += _get_grid_cell_volume(
                        all_uniuqe_coordinates, (x_num, y_num, z_num))

    return volume
