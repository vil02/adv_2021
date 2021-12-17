"""
solution of adv_2021_17
"""
import math
import itertools


def get_max_height(in_min_x, in_max_x, in_min_y, in_max_y, in_vx, in_vy):
    vx, vy = in_vx, in_vy

    def dist_to_target(in_x, in_y):
        def single_dir_dist(in_pos, in_min_t, in_max_t):
            assert in_min_t < in_max_t
            if in_min_t <= in_pos <= in_max_t:
                res = 0
            else:
                res = min(abs(in_min_t-in_pos), abs(in_max_t-in_pos))
            return res
        return single_dir_dist(in_x, in_min_x, in_max_x) + \
            single_dir_dist(in_y, in_min_y, in_max_y)

    def single_move(in_x, in_y):
        nonlocal vx
        nonlocal vy
        res_x = in_x+vx
        res_y = in_y+vy
        if vx != 0:
            if vx > 0:
                vx -= 1
            else:
                vx += 1
        vy -= 1
        return res_x, res_y
    pos_list = []
    cur_x, cur_y = 0, 0
    is_hit = False
    while True:
        # print(cur_x, cur_y, vx, vy, dist_to_target(cur_x, cur_y))
        pos_list.append((cur_x, cur_y))
        cur_x, cur_y = single_move(cur_x, cur_y)
        dist_b = dist_to_target(*pos_list[-1])
        #print(cur_x, cur_y, dist_b)
        if dist_b == 0:
            is_hit = True
            break
        if len(pos_list) > 300:
            dist_a = dist_to_target(*pos_list[-2])
            if dist_a < dist_b and vy <= 0:
                break
    res = -math.inf
    if is_hit:
        print('*')
        res = max(_[1] for _ in pos_list)
    return res


def solve_a(in_str):
    """solution function for part a"""
    max_val = -math.inf
    best_vx = None
    best_vy = None
    for (vx, vy) in itertools.product(range(0, 100), range(-200, 200)):
        cur_val = get_max_height(156, 202, -110, -69, vx, vy)
        #cur_val = get_max_height(20, 30, -10, -5, vx, vy)
        if max_val < cur_val:
            max_val = cur_val
            best_vx = vx
            best_vy = vy
    return max_val



def solve_b(in_str):
    """solution function for part b"""
    max_val = -math.inf
    best_vx = None
    best_vy = None
    hit_numbers = 0
    for (vx, vy) in itertools.product(range(0, 205), range(-350, 350)):
        cur_val = get_max_height(156, 202, -110, -69, vx, vy)
        #cur_val = get_max_height(20, 30, -10, -5, vx, vy)
        if cur_val > -math.inf:
            hit_numbers += 1
    return hit_numbers
