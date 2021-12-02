"""
solution of adv_2021_02
"""


def _parse_command_a(in_command):
    move_type, value = in_command.split(' ')
    if move_type == 'forward':
        res = (int(value), 0)
    elif move_type == 'down':
        res = (0, int(value))
    else:
        assert move_type == 'up'
        res = (0, -int(value))
    return res


def _make_shift(in_pos, in_shift):
    return tuple(a+b for (a, b) in zip(in_pos, in_shift))


def _make_shift_a(in_pos, in_command):
    return _make_shift(in_pos, _parse_command_a(in_command))


def _parse_command_b(in_command):
    move_type, value = in_command.split(' ')
    if move_type == 'forward':
        res = lambda in_pos, in_par=int(value): (in_pos[0]+in_par, in_pos[1]+in_pos[2]*in_par, in_pos[2])
    elif move_type == 'down':
        res = lambda in_pos, in_par=int(value): (in_pos[0], in_pos[1], in_pos[2]+in_par)
    else:
        assert move_type == 'up'
        res = lambda in_pos, in_par=-int(value): (in_pos[0], in_pos[1], in_pos[2]+in_par)
    return res


def _make_shift_b(in_pos, in_command):
    op = _parse_command_b(in_command)
    return op(in_pos)


def solve_a(in_str):
    """solution function for part a"""
    cur_pos = (0, 0)
    for _ in in_str.splitlines():
        cur_pos = _make_shift_a(cur_pos, _)
    return cur_pos[0]*cur_pos[1]


def solve_b(in_str):
    """solution function for part b"""
    cur_pos = (0, 0, 0)
    for _ in in_str.splitlines():
        cur_pos = _make_shift_b(cur_pos, _)
    return cur_pos[0]*cur_pos[1]
