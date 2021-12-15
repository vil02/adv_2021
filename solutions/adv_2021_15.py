"""
solution of adv_2021_15
"""
import copy
import heapq


def parse_input(in_str):
    """
    Parses the input.
    Returns the "list of rows". Each row is a list of numbers
    """
    def proc_row(in_row):
        return [int(_) for _ in in_row]
    res = [proc_row(_) for _ in in_str.splitlines()]
    assert len({len(_) for _ in res}) == 1
    return res


def get_value(in_data, in_pos):
    """
    returns the value storen in in_data in in_pos[0] row and in_pos[1] column
    """
    return in_data[in_pos[0]][in_pos[1]]


def get_all_adjacent_positions(in_data, in_center_pos):
    """returns a list of coordinates of all adjacent positions"""
    def is_correct(in_pos):
        row_num, col_num = in_pos
        return in_pos != in_center_pos \
            and 0 <= row_num < len(in_data) \
            and 0 <= col_num < len(in_data[0])

    search_range = [
        (in_center_pos[0]-1, in_center_pos[1]),
        (in_center_pos[0]+1, in_center_pos[1]),
        (in_center_pos[0], in_center_pos[1]-1),
        (in_center_pos[0], in_center_pos[1]+1)]
    return [_ for _ in search_range if is_correct(_)]


def find_minimum_risk(in_data):
    """
    returns the minimum risk of going from the
    upper-left to the lower-right corner of the in_data
    """
    known_states = [(0, (0, 0))]
    visited = set()
    while True:
        cur_risk, cur_pos = heapq.heappop(known_states)
        if cur_pos in visited:
            continue
        if cur_pos == (len(in_data)-1, len(in_data[cur_pos[0]])-1):
            return cur_risk
        visited.add(cur_pos)
        for new_pos in get_all_adjacent_positions(in_data, cur_pos):
            if new_pos not in visited:
                heapq.heappush(
                    known_states,
                    (cur_risk + get_value(in_data, new_pos), new_pos))


def solve_a(in_str):
    """solution function for part a"""
    return find_minimum_risk(parse_input(in_str))


def make_plus(in_data):
    """
    Increases every value in in_data by 1.
    If the new value is >= 9 it sets it to 1
    """
    def proc_single(in_row):
        return [_ % 9+1 for _ in in_row]
    return [proc_single(_) for _ in in_data]


def extend_data(in_data):
    """
    extends the in_data for the part_b
    """
    def merge_hor(in_data_a, in_data_b):
        return [a+b for (a, b) in zip(in_data_a, in_data_b)]

    def merge_vert(in_data_a, in_data_b):
        return in_data_a+in_data_b
    tmp_data = copy.deepcopy(in_data)
    res_data = copy.deepcopy(in_data)
    extension_size = 4
    for _ in range(extension_size):
        tmp_data = make_plus(tmp_data)
        res_data = merge_hor(res_data, tmp_data)

    tmp_data = copy.deepcopy(res_data)
    for _ in range(extension_size):
        tmp_data = make_plus(tmp_data)
        res_data = merge_vert(res_data, tmp_data)
    return res_data


def solve_b(in_str):
    """solution function for part b"""
    return find_minimum_risk(extend_data(parse_input(in_str)))
