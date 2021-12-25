"""
solution of adv_2021_25
"""


def parse_input(in_str):
    """parses the input into a list of rows"""
    set_x = set()
    set_y = set()
    lines = in_str.splitlines()
    limit_y = len(lines)
    limit_x = len(lines[0])
    for (cur_y, cur_row) in enumerate(in_str.splitlines()):
        for (cur_x, cur_val) in enumerate(cur_row):
            assert cur_x < limit_x
            cur_pos = (cur_x, cur_y)
            if cur_val == '>':
                set_x.add(cur_pos)
            elif cur_val == 'v':
                set_y.add(cur_pos)
            else:
                assert cur_val == '.'

    return (limit_x, limit_y), (set_x, set_y)


def _next_pos(in_limit, in_pos):
    assert in_pos < in_limit
    res_pos = in_pos+1
    if res_pos == in_limit:
        res_pos = 0
    return res_pos


def next_pos_x(in_limit_x, in_pos):
    """calculates the next position of horizontally moving cucumber"""
    return (_next_pos(in_limit_x, in_pos[0]), in_pos[1])


def next_pos_y(in_limit_y, in_pos):
    """calculates the next position of vertically moving cucumber"""
    return (in_pos[0], _next_pos(in_limit_y, in_pos[1]))


def _is_free(in_pos, in_set_x, in_set_y):
    return in_pos not in in_set_x and in_pos not in in_set_y


def can_move_x(in_pos, in_set_x, in_set_y, in_limit_x):
    """checks if it possible to move horizontally from in_pos"""
    return _is_free(next_pos_x(in_limit_x, in_pos), in_set_x, in_set_y)


def can_move_y(in_pos, in_set_x, in_set_y, in_limit_y):
    """checks if it possible to move vertically from in_pos"""
    return _is_free(next_pos_y(in_limit_y, in_pos), in_set_x, in_set_y)


def single_step(in_limit_x, in_limit_y, in_set_x, in_set_y):
    """simulates a single step of all of the cucambers"""
    assert not in_set_x & in_set_y
    new_set_x = set()

    for cur_pos in in_set_x:
        if can_move_x(cur_pos, in_set_x, in_set_y, in_limit_x):
            new_set_x.add(next_pos_x(in_limit_x, cur_pos))
        else:
            new_set_x.add(cur_pos)

    new_set_y = set()
    for cur_pos in in_set_y:
        if can_move_y(cur_pos, new_set_x, in_set_y, in_limit_y):
            new_set_y.add(next_pos_y(in_limit_y, cur_pos))
        else:
            new_set_y.add(cur_pos)
    return new_set_x, new_set_y


def solve_a(in_str):
    """solution function for part a"""
    limits, set_data = parse_input(in_str)
    tmp_set_data = single_step(*limits, *set_data)
    step_num = 1
    while tmp_set_data != set_data:
        step_num += 1
        set_data = tmp_set_data
        tmp_set_data = single_step(*limits, *set_data)
    return step_num
