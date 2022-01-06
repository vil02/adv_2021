"""
solution of adv_2021_10
"""
import statistics


def parse_input(in_str):
    """parses the input of the puzzle to list of strings"""
    return in_str.splitlines()


def _opposite_dict():
    return {')': '(', ']': '[', '>': '<', '}': '{'}


def get_score(in_str):
    """returns a score of the line as described in part a"""
    stack_data = []
    res = None
    for _ in in_str:
        if _ in _opposite_dict().values():
            stack_data.append(_)
        elif stack_data and _ in _opposite_dict() \
                and _opposite_dict()[_] == stack_data[-1]:
            stack_data.pop()
        else:
            res = _
            break
    score_dict = {None: 0, ')': 3, ']': 57, '}': 1197, '>': 25137}
    return score_dict[res]


def solve_a(in_str):
    """solution function for part a"""
    return sum(get_score(_) for _ in parse_input(in_str))


def find_line_completion(in_str):
    """returns the line competion"""
    assert get_score(in_str) == 0
    stack_data = []
    for _ in in_str:
        if _ in _opposite_dict().values():
            stack_data.append(_)
        else:
            assert stack_data and _ in _opposite_dict() \
                and _opposite_dict()[_] == stack_data[-1]
            stack_data.pop()
    res = ''
    inv_opposite_dict = dict(
        zip(_opposite_dict().values(), _opposite_dict().keys()))
    for _ in reversed(stack_data):
        res += inv_opposite_dict[_]
    return res


def get_completion_score(in_str):
    """returns the score of the completion string as in part b"""
    cur_score = 0
    score_dict = {')': 1, ']': 2, '}': 3, '>': 4}
    for _ in in_str:
        cur_score *= 5
        cur_score += score_dict[_]
    return cur_score


def solve_b(in_str):
    """solution function for part b"""
    data = [_ for _ in parse_input(in_str) if get_score(_) == 0]
    score_list = [get_completion_score(find_line_completion(_)) for _ in data]
    return statistics.median(score_list)
