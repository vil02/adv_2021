"""
solution of adv_2021_14
"""


def parse_input(in_str):
    """
    returns the starting string and a dictionary representing production rules
    """

    def proc_single(in_str):
        pattern, result = in_str.split(" -> ")
        assert len(pattern) == 2
        return pattern, result

    lines = in_str.splitlines()
    split_pos = lines.index("")
    start_str = lines[split_pos - 1].strip()
    transforms = dict(proc_single(_) for _ in lines[split_pos + 1 :])
    return start_str, transforms


def calculate_pair_count(in_str):
    """
    returns a histogram for adjacent pairs in in_str
    """
    res = {}
    for _ in range(len(in_str) - 1):
        cur_pair = in_str[_ : _ + 2]
        if cur_pair not in res:
            res[cur_pair] = 0
        res[cur_pair] += 1
    return res


def iterate_pair_count_single(in_pair_count, in_rules):
    """caculates the next iteration for the pair count"""
    res = {}
    for cur_pair in in_pair_count:
        new_char = in_rules[cur_pair]

        if cur_pair[0] + new_char not in res:
            res[cur_pair[0] + new_char] = 0
        res[cur_pair[0] + new_char] += in_pair_count[cur_pair]

        if new_char + cur_pair[1] not in res:
            res[new_char + cur_pair[1]] = 0
        res[new_char + cur_pair[1]] += in_pair_count[cur_pair]
    return res


def pair_count_to_hist(in_pair_count):
    """
    calculates the histogram (for single characters) based on the pair count
    """
    beg_count = {}
    end_count = {}
    for cur_pair in in_pair_count:
        assert len(cur_pair) == 2
        cur_beg = cur_pair[0]
        cur_end = cur_pair[1]
        if cur_beg not in beg_count:
            beg_count[cur_beg] = 0
        beg_count[cur_beg] += in_pair_count[cur_pair]

        if cur_end not in end_count:
            end_count[cur_end] = 0
        end_count[cur_end] += in_pair_count[cur_pair]
    common_keys = set(beg_count) | set(end_count)
    assert sum(beg_count.values()) == sum(end_count.values())
    return {
        _: max(beg_count.get(_, 0), end_count.get(_, 0)) for _ in common_keys
    }


def get_result_value(in_pair_count):
    """
    calculates the resulting value of the puzzle
    """
    hist = pair_count_to_hist(in_pair_count)
    return max(hist.values()) - min(hist.values())


def _proc_data(in_str, in_number_of_iterations):
    cur_str, transforms = parse_input(in_str)
    pair_count = calculate_pair_count(cur_str)
    for _ in range(in_number_of_iterations):
        pair_count = iterate_pair_count_single(pair_count, transforms)
    return get_result_value(pair_count)


def solve_a(in_str):
    """solution function for part a"""
    return _proc_data(in_str, 10)


def solve_b(in_str):
    """solution function for part b"""
    return _proc_data(in_str, 40)
