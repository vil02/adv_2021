"""
solution of adv_2021_17
"""
import functools
import itertools


def get_next_state_x(in_x, in_vel_x):
    """returns the next position and velocity in x-dir"""
    res_x = in_x+in_vel_x
    if in_vel_x != 0:
        if in_vel_x > 0:
            res_vel_x = in_vel_x-1
        else:
            res_vel_x = in_vel_x+1
    else:
        res_vel_x = 0
    return res_x, res_vel_x


def get_next_state_y(in_y, in_vel_y):
    """returns the next position and velocity in y-dir"""
    return in_y+in_vel_y, in_vel_y-1


def is_between(in_val, in_range):
    """checks if in_val is in_range/interval"""
    return in_range[0] <= in_val <= in_range[1]


def is_hit_x(in_x, in_vel_x, in_target_data):
    """checks is in_x/in_vel_x will hit in_target_data"""
    assert in_vel_x >= 0
    if is_between(in_x, in_target_data):
        res = True
    elif in_x > in_target_data[1]:
        res = False
    elif in_x < in_target_data[0] and in_vel_x == 0:
        res = False
    else:
        res = is_hit_x(*get_next_state_x(in_x, in_vel_x), in_target_data)
    return res


def get_next_state(in_pos, in_vel):
    """returns the next position and next velocity"""
    res_pos_x, res_vel_x = get_next_state_x(in_pos[0], in_vel[0])
    res_pos_y, res_vel_y = get_next_state_y(in_pos[1], in_vel[1])
    return ((res_pos_x, res_pos_y), (res_vel_x, res_vel_y))


def simulate(in_pos, in_vel, in_target_data):
    """
    smulates the flight of an object with statrting in_pos and in_vel
    returns the information if it will hit the target and the flight path
    """
    def is_in_target(in_pos, in_target_data):
        return is_between(in_pos[0], in_target_data[0]) \
            and is_between(in_pos[1], in_target_data[1])
    assert 0 < in_target_data[0][0] < in_target_data[0][1]
    assert in_vel[0] >= 0
    path = tuple()
    if is_in_target(in_pos, in_target_data):
        is_hit = True
    elif in_vel[1] < 0 and in_pos[1] < in_target_data[1][0]:
        # too far down
        is_hit = False
    elif in_pos[0] > in_target_data[0][1]:
        # too far right
        is_hit = False
    else:
        tmp_pos, tmp_vel = get_next_state(in_pos, in_vel)
        is_hit, path = simulate(tmp_pos, tmp_vel, in_target_data)
    return is_hit, (in_pos, )+path


@functools.lru_cache(None)
def get_all_hitting_paths(in_target_data):
    """
    returns the list of all paths hittig the target
    """
    def find_min_x_vel(in_target_min_x):
        res = 1
        while (res*(res+1))//2 <= in_target_min_x:
            res += 1
        return res

    def get_x_vel_list(in_target_data_x):
        min_x_vel = find_min_x_vel(in_target_data_x[0])
        max_x_vel = in_target_data_x[1]+1
        return [_ for _ in range(min_x_vel, max_x_vel)
                if is_hit_x(0, _, in_target_data_x)]
    max_y_vel = 2*abs(in_target_data[1][1])+1
    vel_range = itertools.product(
        get_x_vel_list(in_target_data[0]), range(-max_y_vel, max_y_vel))
    res_list = []
    for _ in vel_range:
        is_hit, cur_path = simulate((0, 0), _, in_target_data)
        if is_hit:
            res_list.append(cur_path)
    return res_list


def solve_a(in_target_data):
    """solution function for part a"""
    def get_max_height(in_path):
        return max(_[1] for _ in in_path)
    paths = get_all_hitting_paths(in_target_data)
    return max(get_max_height(_) for _ in paths)


def solve_b(in_target_data):
    """solution function for part b"""
    return len(get_all_hitting_paths(in_target_data))
