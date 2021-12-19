"""
solution of adv_2021_18
"""
import json
import math
import functools
import itertools

def _to_hashable(in_data):
    if isinstance(in_data, int):
        res = in_data
    else:
        assert len(in_data) == 2
        res = tuple(_to_hashable(_) for _ in in_data)
    return res


def parse_input(in_str):
    def proc_single_line(in_line):
        res = json.loads(in_line)
        res = _to_hashable(res)
        # assert get_max_depth(res) <= 4
        return res
    return [proc_single_line(_) for _ in in_str.splitlines()]

def get_max_depth(in_data, cur_depth=0):
    if isinstance(in_data, int):
        res = cur_depth
    else:
        res = max(get_max_depth(_, cur_depth+1) for _ in in_data)
    return res

@functools.lru_cache(None)
def get_node(in_data, in_path):
    assert isinstance(in_path, tuple)
    if not in_path:
        res = in_data
    else:
        res = get_node(in_data[in_path[0]], in_path[1:])
    return res

def find_path_do_expl_pair(in_data):
    def is_atom(in_node):
        return isinstance(in_node, tuple) and \
            isinstance(in_node[0], int) and isinstance(in_node[1], int)    
    def inner(in_path):
        cur_node = get_node(in_data, in_path)
        if is_atom(cur_node):
            res = in_path if len(in_path) >= 4 else None
        elif isinstance(cur_node, int):
            res = None
        else:
            res = inner(in_path+(0,))
            if res is None:
                res = inner(in_path+(1,))
        return res
    return inner(tuple())

def _extend_path(in_data, in_start_path, in_dir):
    assert in_dir in {0, 1}
    res = in_start_path
    while not isinstance(get_node(in_data, res), int):
        res += (in_dir, )
    return res

def find_last(in_data, in_value):
    """
    returns the index of last occurence of in_value in in_data
    """
    assert in_value in in_data
    res = len(in_data)-1
    while in_data[res] != in_value:
        res -= 1
    assert in_data[res] == in_value
    return res

def _find_first_path(in_data, in_path_to_expl, in_dir_a, in_dir_b):
    res = None
    if in_dir_a in in_path_to_expl:
        last_ind = find_last(in_path_to_expl, in_dir_a)
        res = in_path_to_expl[0:last_ind]+(in_dir_b, )
        res = _extend_path(in_data, res, in_dir_a)
    return res    


def find_path_to_first_left(in_data, in_path_to_expl):
    res = _find_first_path(in_data, in_path_to_expl, 1, 0)
    assert res is None or res < in_path_to_expl
    return res
        

def find_path_to_first_right(in_data, in_path_to_expl):
    res = _find_first_path(in_data, in_path_to_expl, 0, 1)
    assert res is None or in_path_to_expl < res
    return res

            
def find_path_to_split(in_data):  
    def inner(in_path):
        cur_node = get_node(in_data, in_path)
        if isinstance(cur_node, int):
            res = in_path if cur_node >= 10 else None
        else:
            res = inner(in_path+(0,))
            if res is None:
                res = inner(in_path+(1,))
        return res
    return inner(tuple())        

def get_updated(in_data, in_update_dict):
    def inner(in_path):
        if in_path in in_update_dict:
            res = in_update_dict[in_path]
        else:
            cur_node = get_node(in_data, in_path)
            if isinstance(cur_node, int):
                res = cur_node
            else:
                res = (inner(in_path+(0, )), inner(in_path+(1, )))
        return res
    return inner(tuple())


def explode(in_data):
    path_to_explode = find_path_do_expl_pair(in_data)
    first_left_path = find_path_to_first_left(in_data, path_to_explode)
    first_right_path = find_path_to_first_right(in_data, path_to_explode)
    exploding_node = get_node(in_data, path_to_explode)
    update_dict = {path_to_explode: 0}
    if first_left_path is not None:
        update_dict[first_left_path] = \
            get_node(in_data, first_left_path)+exploding_node[0]
    if first_right_path is not None:
        update_dict[first_right_path] = \
            get_node(in_data, first_right_path)+exploding_node[1]
    assert len(update_dict) >= 2
    return get_updated(in_data, update_dict)


#def make_split(data):
#    if isinstance(data, int):
#        res = (data//2, math.ceil(data/2)) if data >= 10 else data
#    else:
#        assert len(data) == 2
#        tmp_res = make_split(data[0])
#        if tmp_res != data[0]:
#            res = (tmp_res, data[1])
#        else:
#            res = (data[0], make_split(data[1]))
#    return res
    
def make_split(in_data):
    path_to_split = find_path_to_split(in_data)
    res = in_data
    if path_to_split is not None:
        splited_value = get_node(in_data, path_to_split)
        assert splited_value >= 10
        update_dict = {path_to_split:
            (splited_value//2, math.ceil(splited_value/2))}
        res = get_updated(in_data, update_dict)
    return res

def simplify(in_value):
    def single_simplify(in_value):
        tmp_val = in_value
        if find_path_do_expl_pair(in_value) is not None:
            tmp_val = explode(in_value)
        elif find_path_to_split(in_value) is not None:
            tmp_val = make_split(in_value)
        return tmp_val, in_value != tmp_val    
    tmp_res, has_changed = single_simplify(in_value)
    while has_changed:
        tmp_res, has_changed = single_simplify(tmp_res)
    return tmp_res

def add_values(in_val_a, in_val_b):
    return simplify((in_val_a, in_val_b))

def add_all(in_value_list):
    sum_value = in_value_list[0]
    for _ in in_value_list[1:]:
        sum_value = add_values(sum_value, _)
    return sum_value

def magnitude(in_val):
    def proc_single(in_x):
        if isinstance(in_x, int):
            res = in_x
        else:
            res = magnitude(in_x)
        return res

    return 3*proc_single(in_val[0])+2*proc_single(in_val[1])        

def solve_a(in_str):
    """solution function for part a"""
    return magnitude(add_all(parse_input(in_str)))


def solve_b(in_str):
    """solution function for part b"""
    return max(
        max(magnitude(add_values(a, b)), magnitude(add_values(b, a))) for 
        (a, b) in itertools.combinations(parse_input(in_str), 2))
