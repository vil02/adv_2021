"""
solution of adv_2021_19
"""
import functools
import heapq
import numpy
import itertools

@functools.lru_cache(1)
def get_all_rotations_3d():
    """returns matrices of all 90-degree trotations in 3d"""
    id_mat = numpy.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]])
    x_rot = numpy.array([
        [1, 0, 0],
        [0, 0, -1],
        [0, 1, 0]])
    y_rot = numpy.array([
        [0, 0, 1],
        [0, 1, 0],
        [-1, 0, 0]])
    return [
        id_mat,
        x_rot,
        y_rot,
        x_rot@x_rot,
        x_rot@y_rot,
        y_rot@x_rot,
        y_rot@y_rot,
        x_rot@x_rot@x_rot,
        x_rot@x_rot@y_rot,
        x_rot@y_rot@x_rot,
        x_rot@y_rot@y_rot,
        y_rot@x_rot@x_rot,
        y_rot@y_rot@x_rot,
        y_rot@y_rot@y_rot,
        x_rot@x_rot@x_rot@y_rot,
        x_rot@x_rot@y_rot@x_rot,
        x_rot@x_rot@y_rot@y_rot,
        x_rot@y_rot@x_rot@x_rot,
        x_rot@y_rot@y_rot@y_rot,
        y_rot@x_rot@x_rot@x_rot,
        y_rot@y_rot@y_rot@x_rot,
        x_rot@x_rot@x_rot@y_rot@x_rot,
        x_rot@y_rot@x_rot@x_rot@x_rot,
        x_rot@y_rot@y_rot@y_rot@x_rot]

def get_all_symmetries():
    id_mat = numpy.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]])
    x_sym = numpy.array([
        [-1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]])
    y_sym = numpy.array([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 1]])
    z_sym = numpy.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, -1]])
    return [id_mat, x_sym, y_sym, z_sym]

def get_all_transforms():
    return [a@b for (a, b) in itertools.product(get_all_rotations_3d(), get_all_symmetries())]


def parse_input(in_str):
    """
    returns a list of measurments from each scanner
    """
    res_list = []
    for cur_line in in_str.splitlines():
        if 'scanner' in cur_line:
            scanner_data = []
        elif not cur_line:
            res_list.append(scanner_data)
            scanner_data = []
        else:
            cur_row = tuple(int(_) for _ in cur_line.split(','))
            scanner_data.append(cur_row)
            assert len(scanner_data[-1]) == 3
    return res_list


def extract_x(in_data):
    """returns the list of x-coordinates from the vectors stored in in_data"""
    return [_[0] for _ in in_data]


def extract_xy(in_data):
    """
    returns the list of xy-coordinates from the vectors stored in in_data
    """
    return [_[0:2] for _ in in_data]


def shift_data(in_data, in_shift):
    def proc_single_vec(in_vec):
        return tuple(v+s for (v, s) in zip(in_vec, in_shift))
    return tuple(proc_single_vec(_) for _ in in_data)


def rotate_data(in_rotation, in_data):
    def proc_vec(in_vec):
        return tuple(int(_) for _ in in_vec)
    tmp_data = in_rotation@numpy.array(in_data).transpose()
    return tuple(proc_vec(_) for _ in tmp_data.transpose())


def transform_data(in_rotation, in_data, in_shift):
    return shift_data(rotate_data(in_rotation, in_data), in_shift)


def _get_suitable_shifts(
        in_merged_data, in_scanner_data,
        in_extract_fun, in_shift_fun,
        shift_range):
    def get_shifted(in_data, in_shift):
        return {in_shift_fun(_, in_shift) for _ in in_data}

    def prepare_data(in_data):
        return {_ for _ in in_extract_fun(in_data)}
    merged_proj_data = prepare_data(in_merged_data)
    scanner_proj_data = prepare_data(in_scanner_data)
    raw_res = []
    initial_size = len(merged_proj_data | scanner_proj_data)
    raw_res = []
    for _ in shift_range:
        cur_size = len(merged_proj_data | get_shifted(scanner_proj_data, _))
        if cur_size < initial_size:
            heapq.heappush(raw_res, (cur_size, _))
    res = [_[1] for _ in raw_res]
#    res_size = 10
#    if len(res) > res_size:
#        res = res[0:res_size]
    return res


def get_suitable_x_shifts(in_merged_data, in_scanner_data, x_range):
    return _get_suitable_shifts(
        in_merged_data, in_scanner_data,
        extract_x, lambda x, s: x+s,
        x_range)


def get_suitable_y_shifts(in_merged_data, in_scanner_data, y_range):
    return _get_suitable_shifts(
        in_merged_data, in_scanner_data,
        extract_xy, lambda xy, s: (xy[0], xy[1]+s),
        y_range)


def get_suitable_z_shifts(in_merged_data, in_scanner_data, z_range):
    return _get_suitable_shifts(
        in_merged_data, in_scanner_data,
        lambda xyz, s: (xyz[0], xyz[1], xyz[2]+s),
        z_range)


def merge_single(in_merged_data, in_scanner_data, in_rotation, in_shift):
    tmp_data = transform_data(in_rotation, in_scanner_data, in_shift)
    return in_merged_data | set(tmp_data)


def merge_data(in_scanner_data_list):
    pass

def get_distance_set(in_data):
    def dist(in_vec_a, in_vec_b):
        return sum((a-b)**2 for (a, b) in zip(in_vec_a, in_vec_b))
    return {dist(*_) for _ in itertools.combinations(in_data, 2)}

def find_mostsimilar(in_merged, in_all_scanner_data):
    merged_dist_set = get_distance_set(in_merged)
    res_list = []
    for (scanner_num, scanner_data) in enumerate(in_all_scanner_data):
        cur_dist_set = get_distance_set(scanner_data)
        same_dist_num = len(merged_dist_set & cur_dist_set)
        heapq.heappush(res_list, (-same_dist_num, scanner_num))
    print(res_list)
    res = heapq.heappop(res_list)[1]
    return res

def calculate_result(in_all_data):
    def get_search_range():
        return range(-2600, 2600)

    def select_data(in_merged_data, in_all_scanner_data):
        most_similar = find_mostsimilar(in_merged_data, in_all_scanner_data)
        return in_all_scanner_data[most_similar], \
            in_all_scanner_data[:most_similar]+in_all_scanner_data[most_similar+1:]

    def inner(in_merged_data, in_cur_data, in_all_scanner_data):
        if not in_all_scanner_data:
            print(len(in_merged_data))
        else:
            for cur_rot in get_all_rotations_3d():
                cur_data = rotate_data(cur_rot, in_cur_data)
                x_shifts = get_suitable_x_shifts(in_merged_data, cur_data, get_search_range())
                for x_shift in x_shifts:
                    cur_data_xy = shift_data(cur_data, (x_shift, 0, 0))
                    y_shifts = get_suitable_y_shifts(in_merged_data, cur_data_xy, get_search_range())
                    for y_shift in y_shifts:
                        cur_data_xyz =  shift_data(cur_data, (x_shift, y_shift, 0))
                        z_shifts = get_suitable_y_shifts(in_merged_data, cur_data_xyz, get_search_range())
                        for z_shift in z_shifts:
                            new_merged = merge_single(in_merged_data, in_cur_data, cur_rot, (x_shift, y_shift, z_shift))
                            inner(
                                *select_data(new_merged, in_all_scanner_data))
    tmp_start_data = set(in_all_data[0])
    inner(tmp_start_data, *select_data(tmp_start_data, in_all_data[1:]))


def solve_a(in_str):
    """solution function for part a"""
    calculate_result(parse_input(in_str))
    return -100


# def solve_b(in_str):
#     """solution function for part b"""
#     pass
