"""
solution of adv_2021_12
"""
import copy


def parse_input(in_str):
    """
    parses the input string in_str into a dictionary representing a graph
    res['node_name'] is a list of all nodes,
    which can be direcly accessed from the given one
    """
    result = {}

    def update_res(in_first_cave, in_second_cave):
        if in_first_cave not in result:
            result[in_first_cave] = []
        result[in_first_cave].append(in_second_cave)
    for _ in in_str.splitlines():
        cave_a, cave_b = _.split('-')
        update_res(cave_a, cave_b)
        update_res(cave_b, cave_a)
    return result


def is_cave_small(in_cave):
    """checks if the in_case is small"""
    return in_cave.islower()


def find_number_of_paths_a(in_data):
    """
    returns the number of paths as described in part a
    """
    path_list = []

    def inner(cur_cave, cur_path, visited_small_caves):
        if cur_cave == 'end':
            path_list.append(cur_path)
        else:
            for new_cave in in_data[cur_cave]:
                if (is_cave_small(new_cave) and new_cave not in cur_path):
                    inner(
                        new_cave, cur_path+[new_cave],
                        visited_small_caves | set(new_cave))
                elif not is_cave_small(new_cave):
                    inner(new_cave, cur_path+[new_cave], visited_small_caves)
    inner('start', ['start'], set())
    return len(path_list)


def find_number_of_paths_b(in_data):
    """
    returns the number of paths as described in part b
    """
    path_list = []

    def is_worth_visit(in_cave, in_visited_dict):
        assert is_cave_small(in_cave)
        return in_cave not in in_visited_dict \
            or all(_ < 2 for _ in in_visited_dict.values())

    def inner(cur_cave, cur_path, visited_small_caves):
        if cur_cave == 'end':
            path_list.append(cur_path)
        else:
            for new_cave in in_data[cur_cave]:
                if is_cave_small(new_cave) and new_cave != 'start' \
                        and is_worth_visit(new_cave, visited_small_caves):
                    tmp_visited_small_caves = \
                        copy.deepcopy(visited_small_caves)
                    if new_cave in tmp_visited_small_caves:
                        tmp_visited_small_caves[new_cave] += 1
                    else:
                        tmp_visited_small_caves[new_cave] = 1
                    inner(
                        new_cave, cur_path+[new_cave], tmp_visited_small_caves)
                elif not is_cave_small(new_cave):
                    inner(new_cave, cur_path+[new_cave], visited_small_caves)
    inner('start', ['start'], {})
    return len(path_list)


def solve_a(in_str):
    """solution function for part a"""
    return find_number_of_paths_a(parse_input(in_str))


def solve_b(in_str):
    """solution function for part b"""
    return find_number_of_paths_b(parse_input(in_str))
