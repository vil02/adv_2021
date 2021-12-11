"""
solution of adv_2021_11
"""
import itertools
import copy


def parse_input(in_str):
    """parses the input into a list of rows"""
    def proc_single_line(in_line):
        return [int(_) for _ in in_line]
    res = [proc_single_line(_) for _ in in_str.splitlines()]
    assert len(set(len(_) for _ in res)) == 1
    return res


def get_all_adjacent_positions(in_data, in_center_pos):
    """returns a list of coordinates of all adjacent positions"""
    def is_correct(in_pos):
        row_num, col_num = in_pos
        return in_pos != in_center_pos \
            and 0 <= row_num < len(in_data) \
            and 0 <= col_num < len(in_data[0])

    search_range = itertools.product(
        range(in_center_pos[0]-1, in_center_pos[0]+2),
        range(in_center_pos[1]-1, in_center_pos[1]+2))
    return [_ for _ in search_range if is_correct(_)]


def get_value(in_data, in_pos):
    """
    returns the value stored as position in_pos =(row_num, col_num) in in_data
    """
    return in_data[in_pos[0]][in_pos[1]]


def set_value(data, in_pos, in_val):
    """
    sets the value in data at posiion in_pos to in_val
    """
    data[in_pos[0]][in_pos[1]] = in_val


def single_step(in_data):
    """
    simulates one energy step
    returns the new power data and the number of flashes
    """
    res_data = copy.deepcopy(in_data)
    flashed = set()
    search_range = list(
        itertools.product(range(0, len(in_data)), range(0, len(in_data[0]))))
    for cur_pos in search_range:
        set_value(res_data, cur_pos, get_value(in_data, cur_pos)+1)

    was_change = True
    while was_change:
        was_change = False
        for cur_pos in search_range:
            if cur_pos not in flashed and get_value(res_data, cur_pos) > 9:
                for _ in get_all_adjacent_positions(in_data, cur_pos):
                    set_value(res_data, _, get_value(res_data, _)+1)
                flashed.add(cur_pos)
                was_change = True
    for cur_pos in flashed:
        set_value(res_data, cur_pos, 0)
    return res_data, len(flashed)


def solve_a(in_str):
    """solution function for part a"""
    data = parse_input(in_str)
    total_count = 0
    for _ in range(100):
        data, cur_count = single_step(data)
        total_count += cur_count
    return total_count


def solve_b(in_str):
    """solution function for part b"""
    data = parse_input(in_str)
    total_size = sum(len(_) for _ in data)
    cur_step_num = 0
    cur_count = 0
    while total_size != cur_count:
        data, cur_count = single_step(data)
        cur_step_num += 1
    return cur_step_num
