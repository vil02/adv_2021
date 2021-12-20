"""
solution of adv_2021_20
"""
import functools


def parse_input(in_str):
    """parses the input of the puzzle"""
    def proc_alg_data(in_str):
        res = set()
        for (bit_num, state) in enumerate(in_str):
            if state == '#':
                res.add(bit_num)
        return frozenset(res)

    def proc_image_data(in_str_list):
        res = set()
        assert len(set(len(_) for _ in in_str_list)) == 1
        for (y_pos, cur_row) in enumerate(reversed(in_str_list)):
            for (x_pos, state) in enumerate(cur_row):
                if state == '#':
                    res.add((x_pos, y_pos))
        return frozenset(res)

    str_line_list = in_str.splitlines()
    split_pos = str_line_list.index('')
    alg_data_str = ''.join(str_line_list[:split_pos])
    assert len(alg_data_str) == 512
    return proc_alg_data(alg_data_str), \
        proc_image_data(str_line_list[split_pos+1:])


def get_all_neighbours(in_pos):
    """
    Returns the list of all of the neighbouring fields.
    Result is ordered from top-left to bottom-right.
    """
    def make_shift(in_pos, in_shift):
        return tuple(p+s for (p, s) in zip(in_pos, in_shift))
    shift_list = (
        (-1, 1), (0, 1), (1, 1),
        (-1, 0), (0, 0), (1, 0),
        (-1, -1), (0, -1), (1, -1))
    return tuple(make_shift(in_pos, _) for _ in shift_list)


def get_bounds(in_pixel_data):
    """
    returns the bounds of the binary image
    represented by the set in_pixel_data
    """
    min_x = min(_[0] for _ in in_pixel_data)
    max_x = max(_[0] for _ in in_pixel_data)
    min_y = min(_[1] for _ in in_pixel_data)
    max_y = max(_[1] for _ in in_pixel_data)
    return min_x, max_x, min_y, max_y


def _make_double_iteration(in_alg_data, in_pixel_data):
    def to_char(in_val):
        return '1' if in_val else '0'

    @functools.lru_cache(None)
    def get_pixel_inner(in_pos, in_iteration):
        if in_iteration == 0:
            res = in_pos in in_pixel_data
        else:
            bin_val_str = ''.join(
                to_char(get_pixel_inner(_, in_iteration-1))
                for _ in get_all_neighbours(in_pos))
            res = int(bin_val_str, 2) in in_alg_data
        return res
    res = set()
    min_x, max_x, min_y, max_y = get_bounds(in_pixel_data)
    margin = 2
    for cur_x in range(min_x-margin, max_x+margin+1):
        for cur_y in range(min_y-margin, max_y+margin+1):
            if get_pixel_inner((cur_x, cur_y), 2):
                res.add((cur_x, cur_y))
    return res


def _count_pixels(in_alg_data, in_pixel_data, in_max_iteration):
    assert in_max_iteration % 2 == 0
    pixel_data = in_pixel_data
    for _ in range(in_max_iteration//2):
        pixel_data = _make_double_iteration(in_alg_data, pixel_data)
    return len(pixel_data)


def solve_a(in_str):
    """solution function for part a"""
    alg_data, pixel_data = parse_input(in_str)
    return _count_pixels(alg_data, pixel_data, 2)


def solve_b(in_str):
    """solution function for part b"""
    alg_data, pixel_data = parse_input(in_str)
    return _count_pixels(alg_data, pixel_data, 50)
