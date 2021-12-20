"""
solution of adv_2021_17
"""
import functools
import itertools


def get_next_state(in_pos, in_vel):
    """returns the next position and nect velocity"""
    res_pos = tuple(p+v for (p, v) in zip(in_pos, in_vel))
    if in_vel[0] != 0:
        if in_vel[0] > 0:
            res_vel_x = in_vel[0]-1
        else:
            res_vel_x = in_vel[0]+1
    else:
        res_vel_x = in_vel[0]
    res_vel = (res_vel_x, in_vel[1]-1)
    return (res_pos, res_vel)


def simulate(in_pos, in_vel, in_target_data):
    """
    smulates the flight of an object with statrting in_pos and in_vel
    returns the information if it will hit the target and the flight path
    """
    def is_in_target(in_pos, in_target_data):
        def is_between(in_val, in_range):
            return in_range[0] <= in_val <= in_range[1]
        return all(
            is_between(in_pos[_], in_target_data[_])
            for _ in range(len(in_pos)))
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
        if (res*(res+1))//2 <= in_target_min_x:
            res += 1
        return res-1
    min_x_vel = find_min_x_vel(in_target_data[0][0])
    max_x_vel = in_target_data[0][1]+1
    max_y_vel = 2*abs(in_target_data[1][1])+1
    vel_range = itertools.product(
        range(min_x_vel, max_x_vel), range(-max_y_vel, max_y_vel))
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
