"""
solution of adv_2021_08
"""
import copy


def parse_input_a(in_str):
    """parses input for part a"""
    def proc_single_line(in_line):
        _, part_b = in_line.split(' | ')
        return part_b.split()
    res = []
    for _ in in_str.splitlines():
        res += proc_single_line(_)
    return res


def solve_a(in_str):
    """solution function for part a"""
    data = parse_input_a(in_str)
    return sum(1 for _ in data if len(_) in [2, 4, 3, 7])


def parse_input_b(in_str):
    """parses input for part b"""
    def proc_single_line(in_line):
        part_a, part_b = in_line.split(' | ')
        return part_a.split(), part_b.split()
    return [proc_single_line(_) for _ in in_str.splitlines()]


def _display_numbers():
    return [
        "abcefg",
        "cf",
        "acdeg",
        "acdfg",
        "bcdf",
        "abdfg",
        "abdefg",
        "acf",
        "abcdefg",
        "abcdfg"]


def _display_numbers_set():
    return set(_display_numbers())


def apply_permutation(in_perm_data, in_str_list):
    """applies given permutation"""
    def proc_single_str(in_str):
        return ''.join(sorted(in_perm_data[_] for _ in in_str))
    return [proc_single_str(_) for _ in in_str_list]


def _find_bounds(in_2, in_3, in_4, in_7):
    set_2, set_3, set_4, set_7 = [set(_) for _ in [in_2, in_3, in_4, in_7]]
    assert len(set_2) == 2
    assert len(set_3) == 3
    assert len(set_4) == 4
    assert len(set_7) == 7

    res = {}
    val_of_a = list(set_3-set_2)
    assert len(val_of_a) == 1
    val_of_a = val_of_a[0]
    res[val_of_a] = 'a'
    set_3.remove(val_of_a)
    assert val_of_a not in set_4
    set_7.remove(val_of_a)
    assert set_2 == set_3
    for _ in set_2:
        res[_] = 'cf'
        set_4.remove(_)
        set_7.remove(_)
    for _ in set_4:
        res[_] = 'bd'
        set_7.remove(_)
    for _ in set_7:
        res[_] = 'deg'
    assert set(''.join(res.values())) == set(''.join(_display_numbers()))
    assert set(res.keys()) == set(''.join(_display_numbers()))
    res = {key: set(val) for (key, val) in res.items()}
    return res


def _find_all_permutations_with_bounds(in_bounds):
    def inner(cur_perm, available_keys, cur_bounds):
        if not available_keys:
            yield cur_perm
        else:
            cur_key = available_keys[0]
            new_perm = copy.deepcopy(cur_perm)
            for cur_val in in_bounds[cur_key]:
                if cur_val not in cur_perm.values():
                    new_perm[cur_key] = cur_val
                    new_bounds = copy.deepcopy(cur_bounds)
                    for _ in cur_bounds:
                        new_bounds[_].discard(cur_val)
                    for _ in inner(new_perm, available_keys[1:], new_bounds):
                        yield _
    return inner({}, list(in_bounds.keys()), in_bounds)


def find_pemutation(in_str_list):
    """finds pemutation of the wires"""
    def find_str_of_len(in_len):
        res = [_ for _ in in_str_list if len(_) == in_len]
        assert len(res) == 1
        return res[0]

    bounds = _find_bounds(*[find_str_of_len(_) for _ in [2, 3, 4, 7]])
    for perm_data in _find_all_permutations_with_bounds(bounds):
        cur_displays = apply_permutation(perm_data, in_str_list)
        if set(cur_displays) == _display_numbers_set():
            res = perm_data
            break
    return res


def get_value(in_str_list):
    """returns a displayed number"""
    digit_list = [str(_display_numbers().index(_)) for _ in in_str_list]
    return int(''.join(digit_list))


def solve_single_line(in_part_a, in_part_b):
    """solves single line from part b"""
    cur_displays = apply_permutation(find_pemutation(in_part_a), in_part_b)
    return get_value(cur_displays)


def solve_b(in_str):
    """solution function for part b"""
    return sum(solve_single_line(*_) for _ in parse_input_b(in_str))
