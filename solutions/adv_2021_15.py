"""
solution of adv_2021_15
"""
import itertools
import functools
import copy
import heapq


def parse_input(in_str):
    def proc_row(in_row):
        return [int(_) for _ in in_row]
    return [proc_row(_) for _ in in_str.splitlines()]


def get_value(in_data, in_pos):
    return in_data[in_pos[0]][in_pos[1]]


# def get_new_fields(in_data, in_pos):
#     # res = []
#     # if in_pos[0] < len(in_data)-1:
#     #     res.append((in_pos[0]+1, in_pos[1]))
#     # if in_pos[1] < len(in_data[0])-1:
#     #     res.append((in_pos[0], in_pos[1]+1))


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


# def find_minimum_risk(in_data):
#     visited = {}
#
#     def inner(cur_pos, in_path):
#         if (cur_pos, in_path) in visited:
#             res = visited[(cur_pos, in_path)]
#         elif cur_pos[0] == len(in_data)-1 and cur_pos[1] == len(in_data[-1])-1:
#             res = get_value(in_data, cur_pos)
#         else:
#             min_val = math.inf
#             for _ in get_all_adjacent_positions(in_data, cur_pos):
#                 if _ not in in_path:
#                     min_val = min(min_val, inner(_, tuple(list(in_path)+[_])))
#             res = get_value(in_data, cur_pos) + min_val
#             visited[(cur_pos, in_path)] = res
#         return res
#
#     res =inner((0, 0), ((0, 0),))-get_value(in_data, (0, 0))
#     print(visited)
#     return res
#
# def find_minimum_risk(in_data):
#     visited = {}
#
#     def inner(cur_pos):
#         if cur_pos in visited:
#             res = visited[cur_pos]
#         elif cur_pos[0] == len(in_data)-1 and cur_pos[1] == len(in_data[-1])-1:
#             res = get_value(in_data, cur_pos)
#         else:
#             min_val = math.inf
#             for _ in get_all_adjacent_positions(in_data, cur_pos):
#                 min_val = min(min_val, inner(_))
#             res = get_value(in_data, cur_pos) + min_val
#             visited[cur_pos] = res
#         return res
#
#     return inner((0, 0))-get_value(in_data, (0, 0))

def find_minimum_risk(in_data):
    known_states = [(0, (0, 0))]

    visited = set()
    while True:
        cur_risk, cur_pos = heapq.heappop(known_states)
        if cur_pos in visited:
            continue
        if cur_pos == (len(in_data)-1, len(in_data[0])-1):
            return cur_risk
        visited.add(cur_pos)
        for new_pos in get_all_adjacent_positions(in_data, cur_pos):
            if new_pos not in visited:
                heapq.heappush(
                    known_states,
                    (cur_risk + get_value(in_data, new_pos), new_pos))



def solve_a(in_str):
    """solution function for part a"""
    data = parse_input(in_str)
    return find_minimum_risk(data)


def make_plus(in_data):
    def proc_single(in_row):
        def proc_val(in_val):
            res = in_val+1
            if res >= 10:
                res = 1
            return res
        return [proc_val(_) for _ in in_row]
    return [proc_single(_) for _ in in_data]


def merge_hor(in_data_a, in_data_b):
    res = [a+b for (a, b) in zip(in_data_a, in_data_b)]

    return res


def merge_vert(in_data_a, in_data_b):
    res = in_data_a+in_data_b

    return res

def generate_big_data(in_data):
    tmp_data = copy.deepcopy(in_data)
    res_data = copy.deepcopy(in_data)
    for _ in range(4):
        tmp_data = make_plus(tmp_data)
        res_data = merge_hor(res_data, tmp_data)

    tmp_data = copy.deepcopy(res_data)
    for _ in range(4):
        tmp_data = make_plus(tmp_data)
        res_data = merge_vert(res_data, tmp_data)
    return res_data

def solve_b(in_str):
    """solution function for part b"""
    data = parse_input(in_str)
    data = generate_big_data(data)
    return find_minimum_risk(data)
