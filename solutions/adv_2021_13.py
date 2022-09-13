"""
solution of adv_2021_13
"""


def parse_input(in_str):
    """
    Parses the input of the puzzle.
    returns the set of all positions and the list of folds
    """

    def proc_pos_str(in_str):
        x_pos, y_pos = in_str.split(",")
        return int(x_pos), int(y_pos)

    def proc_fold_str(in_str):
        start_str = "fold along "
        assert in_str.startswith(start_str)
        fold_str = in_str[len(start_str) :]
        axis_str, pos_str = fold_str.split("=")
        return axis_str, int(pos_str)

    lines = in_str.splitlines()
    blank_line_num = lines.index("")
    positions = {proc_pos_str(_) for _ in lines[0:blank_line_num]}
    folds = [proc_fold_str(_) for _ in lines[blank_line_num + 1 :]]
    return positions, folds


def to_str(in_data):
    """
    returns a string illustrating the position set in_data
    """
    x_max = max(_[0] for _ in in_data)
    y_max = max(_[1] for _ in in_data)
    res = [["." for _ in range(x_max + 1)] for _ in range(y_max + 1)]
    for (x_pos, y_pos) in in_data:
        res[y_pos][x_pos] = "#"
    return "\n".join(["".join(_ for _ in cur_row) for cur_row in res])


def _transform_pos(in_pos, in_fold_pos):
    res_pos = in_pos
    if in_pos > in_fold_pos:
        res_pos = in_fold_pos - abs(in_pos - in_fold_pos)
    return res_pos


def _transform_x(in_pos, in_fold_pos):
    return _transform_pos(in_pos[0], in_fold_pos), in_pos[1]


def _transform_y(in_pos, in_fold_pos):
    return in_pos[0], _transform_pos(in_pos[1], in_fold_pos)


def make_transform(in_pos, in_fold_type, in_fold_pos):
    """makes a transformation of a single point"""
    if in_fold_type == "x":
        res = _transform_x(in_pos, in_fold_pos)
    else:
        assert in_fold_type == "y"
        res = _transform_y(in_pos, in_fold_pos)
    return res


def make_fold(in_data, in_fold):
    """makes a fold for all of the point"""
    return {make_transform(_, *in_fold) for _ in in_data}


def solve_a(in_str):
    """solution function for part a"""
    pos_data, fold_list = parse_input(in_str)
    return len(make_fold(pos_data, fold_list[0]))


def solve_b(in_str):
    """solution function for part b"""
    pos_data, fold_list = parse_input(in_str)
    for _ in fold_list:
        pos_data = make_fold(pos_data, _)
    return to_str(pos_data)
