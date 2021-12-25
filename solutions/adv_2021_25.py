"""
solution of adv_2021_25
"""


def parse_input(in_str):
    """parses the input into a list of rows"""
    res = tuple(tuple(cur_row) for cur_row in in_str.splitlines())
    assert len(set(len(_) for _ in res)) == 1
    assert all(set(_).issubset({'.', 'v', '>'}) for _ in res)
    return res


def next_pos_x(in_data, in_pos):
    """calculates the next position of horizontally moving cucumber"""
    res = [in_pos[0], in_pos[1]+1]
    if res[1] >= len(in_data[in_pos[0]]):
        res[1] = 0
    return res


def next_pos_y(in_data, in_pos):
    """calculates the next position of vertically moving cucumber"""
    res = [in_pos[0]+1, in_pos[1]]
    if res[0] >= len(in_data):
        res[0] = 0
    return res


def get_value(in_data, in_pos):
    """
    returns the position stored in in_data
    in row in_pos[0] and column in_pos[1]
    """
    return in_data[in_pos[0]][in_pos[1]]


def set_value(data, in_pos, in_val):
    """
    sets value in data at position in_pos to in_val
    """
    data[in_pos[0]][in_pos[1]] = in_val


def _is_empty(in_data, in_pos):
    return get_value(in_data, in_pos) == '.'


def can_move_x(in_data, in_pos):
    """checks if it possible to move horizontally from in_pos"""
    return _is_empty(in_data, next_pos_x(in_data, in_pos))


def can_move_y(in_data, in_pos):
    """checks if it possible to move vertically from in_pos"""
    return _is_empty(in_data, next_pos_y(in_data, in_pos))


def _to_pos(in_pos_x, in_pos_y):
    return (in_pos_y, in_pos_x)


def single_step(in_data):
    """simulates a single step of all of the cucambers"""
    res_hor = [['.' for _ in cur_row] for cur_row in in_data]
    for (pos_y, cur_row) in enumerate(in_data):
        for (pos_x, cur_val) in enumerate(cur_row):
            cur_pos = _to_pos(pos_x, pos_y)
            if cur_val == '>':
                if can_move_x(in_data, cur_pos):
                    set_value(res_hor, next_pos_x(in_data, cur_pos), '>')
                else:
                    set_value(res_hor, cur_pos, '>')
            elif cur_val == 'v':
                set_value(res_hor, cur_pos, 'v')

    res_ver = [['.' for _ in cur_row] for cur_row in res_hor]
    for (pos_y, cur_row) in enumerate(res_hor):
        for (pos_x, cur_val) in enumerate(cur_row):
            cur_pos = _to_pos(pos_x, pos_y)
            if cur_val == '>':
                set_value(res_ver, cur_pos, '>')
            elif cur_val == 'v':
                if can_move_y(res_hor, cur_pos):
                    set_value(res_ver, next_pos_y(res_hor, cur_pos), 'v')
                else:
                    set_value(res_ver, cur_pos, 'v')
    return tuple(tuple(_) for _ in res_ver)


def solve_a(in_str):
    """solution function for part a"""
    data = parse_input(in_str)
    tmp_data = single_step(data)
    step_num = 1
    while tmp_data != data:
        step_num += 1
        data = tmp_data
        tmp_data = single_step(data)
    return step_num
