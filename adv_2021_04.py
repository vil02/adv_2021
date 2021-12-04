"""
solution of adv_2021_04
"""


def _board_size():
    return 5


def _parse_input(in_str):
    def proc_square(in_lines):
        assert len(in_lines) == _board_size()
        res = []
        for cur_line in in_lines:
            cur_line_res = []
            for cur_num in cur_line.split(' '):
                if cur_num != ' ' and cur_num != '':
                    cur_line_res.append((int(cur_num), False))
            assert(len(cur_line_res)) == _board_size()
            res.append(cur_line_res)
        return res
    lines = in_str.splitlines()
    lines = [_ for _ in lines if len(_) > 1]
    numbers = [int(_) for _ in lines[0].split(',')]
    lines = lines[1:]
    assert len(lines) % _board_size() == 0
    res = []
    for start_num in range(0, len(lines), _board_size()):
        res.append(proc_square(lines[start_num:start_num+_board_size()]))
    # print(res)
    return numbers, res


def mark(in_square, in_num):
    res_lines = []
    for cur_line in in_square:
        tmp_line = []
        for _ in cur_line:
            if _[0] == in_num:
                tmp_line.append((_[0], True))
            else:
                tmp_line.append(_)
        res_lines.append(tmp_line)
    return res_lines


def check_if_wins(in_square):
    def is_row_marked(in_row_num):
        return all(_[1] for _ in in_square[in_row_num])

    def is_col_marked(in_col_num):
        cur_col = [in_square[_][in_col_num] for _ in range(_board_size())]
        return all(_[1] for _ in cur_col)
    return any(is_row_marked(_) for _ in range(_board_size())) or \
        any(is_col_marked(_) for _ in range(_board_size()))


def find_winning(in_data):
    res = None
    for _ in in_data:
        if check_if_wins(_):
            res = _
            break
    return res

def count_unmarked_sum(in_data):
    return sum(sum(_[0] for _ in cur_row if not _[1]) for cur_row in in_data)

def solve_a(in_str):
    """solution function for part a"""
    numbers, data = _parse_input(in_str)
    for cur_num in numbers:
        data = [mark(_, cur_num) for _ in data]
        winner = find_winning(data)
        if winner is not None:
            return count_unmarked_sum(winner)*cur_num
    return -2


def solve_b(in_str):
    """solution function for part b"""
    numbers, data = _parse_input(in_str)
    last_winner_score = None
    for cur_num in numbers:
        data = [mark(_, cur_num) for _ in data]
        winner = find_winning(data)
        if winner is not None:
            last_winner_score = count_unmarked_sum(winner)*cur_num
        data = [_ for _ in data if not check_if_wins(_)]
    return last_winner_score
