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


def is_pos_valid(in_data, in_row, in_col):
    """checks if the position (in_row, in_col) is valid"""
    return 0 <= in_row < len(in_data) and 0 <= in_col < len(in_data[in_row])


def get_value(in_data, in_pos):
    """returns the value form in_data at in_pos"""
    return in_data[in_pos[0]][in_pos[1]]


def get_adjacent_values(in_data, in_row, in_col):
    """
    returns all of the values in the neighbouring cells (diagonal included)
    """
    search_range = set(itertools.product(
        range(in_row-1, in_row+2),
        range(in_col-1, in_col+2)))
    search_range.remove((in_row, in_col))
    return [get_value(in_data, (row, col)) for
            (row, col) in search_range
            if is_pos_valid(in_data, row, col)]


def is_minimum(in_data, in_row, in_col):
    """
    checks if the value in_data[in_row][in_col] is a local minimum
    """
    return all(
        in_data[in_row][in_col] < _
        for _ in get_adjacent_values(in_data, in_row, in_col))


def solve_a(in_str):
    """solution function for part a"""
    data = parse_input(in_str)
    search_range = itertools.product(
        range(0, len(data)),
        range(0, len(data[0])))
    return sum(
        1+get_value(data, _) for
        _ in search_range if is_minimum(data, *_))


def get_small_neighours(in_data, in_row, in_col):
    """returns the list of neighbouring positions (no diagonal)"""
    search_range = [
        (in_row-1, in_col),
        (in_row+1, in_col),
        (in_row, in_col-1),
        (in_row, in_col+1)]
    return [(row, col) for
            (row, col) in search_range
            if is_pos_valid(in_data, row, col)]


def get_all_basins(in_data):
    """
    Returns a list of all basins.
    Each basin is represented as a set of points.
    """
    visited_set = set()

    def single_step(in_pos):
        if in_pos not in visited_set:
            visited_set.add(in_pos)
            for new_pos in get_small_neighours(in_data, *in_pos):
                if get_value(in_data, new_pos) != 9:
                    single_step(new_pos)

    basins = []
    for start_pos in itertools.product(
            range(len(in_data)), range(len(in_data[0]))):
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
