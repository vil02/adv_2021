"""
solutions of adv_2021_21
"""
import itertools
import functools
import copy


def parse_input(in_str):
    """returns the starting positions of the players"""

    def proc_single_line(in_line_str):
        piece_list = in_line_str.split(" ")
        return int(piece_list[-1])

    return [proc_single_line(_) for _ in in_str.splitlines()]


def simulate_a(in_pos_list):
    """
    simulates the game in part a
    """

    def test_die():
        cur_val = 0
        while True:
            yield 1 + (cur_val % 100)
            cur_val += 1

    score_list = [0 for _ in in_pos_list]
    pos_list = copy.deepcopy(in_pos_list)
    cur_player = 0
    cur_die = test_die()
    roll_num = 0
    while max(score_list) < 1000:
        shift_val = next(cur_die) + next(cur_die) + next(cur_die)
        pos_list[cur_player] = (pos_list[cur_player] + shift_val - 1) % 10 + 1
        score_list[cur_player] += pos_list[cur_player]
        roll_num += 3
        cur_player += 1
        cur_player %= len(in_pos_list)
    return roll_num * min(score_list)


def solve_a(in_str):
    """solution function for part a"""
    return simulate_a(parse_input(in_str))


def simulate_b(in_pos_a, in_pos_b):
    """
    returns the number of universes in which the winning player would win
    """
    shift_dict = {}
    for _ in itertools.product([1, 2, 3], repeat=3):
        cur_sum = sum(_)
        if cur_sum in shift_dict:
            shift_dict[cur_sum] += 1
        else:
            shift_dict[cur_sum] = 1

    @functools.lru_cache(None)
    def inner(in_data_a, in_data_b):
        pos_a, score_a = in_data_a
        win_uni_a = 0
        win_uni_b = 0
        for (cur_shift, cur_count) in shift_dict.items():
            new_pos = (pos_a + cur_shift - 1) % 10 + 1
            new_score = score_a + new_pos
            if new_score >= 21:
                win_uni_a += cur_count
            else:
                tmp_b, tmp_a = inner(in_data_b, (new_pos, new_score))
                win_uni_a += cur_count * tmp_a
                win_uni_b += cur_count * tmp_b
        return win_uni_a, win_uni_b

    return max(inner((in_pos_a, 0), (in_pos_b, 0)))


def solve_b(in_str):
    """solution function for part b"""
    return simulate_b(*parse_input(in_str))
