"""
solution of adv_2021_09
"""
import itertools


def parse_input(in_str):
    """parses the input into a list of rows"""
    def proc_single_line(in_line):
        return [int(_) for _ in in_line]
    res = [proc_single_line(_) for _ in in_str.splitlines()]
    assert len(set(len(_) for _ in res)) == 1
    return res


def is_pos_valid(in_data, in_pos):
    """checks if the position in_pos is valid"""
    in_row, in_col = in_pos
    return 0 <= in_row < len(in_data) and 0 <= in_col < len(in_data[in_row])


def get_value(in_data, in_pos):
    """returns the value form in_data at in_pos"""
    return in_data[in_pos[0]][in_pos[1]]


def get_small_neighours(in_data, in_pos):
    """returns the list of neighbouring positions (no diagonal)"""
    in_row, in_col = in_pos
    search_range = [
        (in_row-1, in_col),
        (in_row+1, in_col),
        (in_row, in_col-1),
        (in_row, in_col+1)]
    return [_ for _ in search_range if is_pos_valid(in_data, _)]


def get_adjacent_values(in_data, in_pos):
    """returns all of the values in the neighbouring cells (no diagonal)"""
    return [get_value(in_data, _)
            for _ in get_small_neighours(in_data, in_pos)]


def is_minimum(in_data, in_pos):
    """
    checks if the value in_data[in_row][in_col] is a local minimum
    """
    return all(
        get_value(in_data, in_pos) < _
        for _ in get_adjacent_values(in_data, in_pos))


def _get_full_search_range(in_data):
    return itertools.product(range(0, len(in_data)), range(0, len(in_data[0])))


def solve_a(in_str):
    """solution function for part a"""
    data = parse_input(in_str)
    return sum(
        1+get_value(data, _) for
        _ in _get_full_search_range(data) if is_minimum(data, _))


def get_all_basins(in_data):
    """
    Returns a list of all basins.
    Each basin is represented as a set of points.
    """
    visited_set = set()

    def single_step(in_pos):
        if in_pos not in visited_set:
            visited_set.add(in_pos)
            for new_pos in get_small_neighours(in_data, in_pos):
                if get_value(in_data, new_pos) != 9:
                    single_step(new_pos)

    basins = []
    for start_pos in _get_full_search_range(in_data):
        if get_value(in_data, start_pos) != 9 and \
                all(start_pos not in _ for _ in basins):
            single_step(start_pos)
            basins.append(visited_set)
            visited_set = set()
    return basins


def solve_b(in_str):
    """solution function for part b"""
    data = parse_input(in_str)
    basins = get_all_basins(data)
    basins.sort(key=len)
    assert len(basins) >= 3
    return len(basins[-1])*len(basins[-2])*len(basins[-3])
