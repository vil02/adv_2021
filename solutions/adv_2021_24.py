"""
solution of adv_2021_24
"""
import functools


def parse_input(in_str):
    """parses the input"""

    def proc_registers(in_str_list):
        res = []
        for _ in in_str_list:
            if _ in ["x", "y", "z", "w"]:
                res.append(_)
            else:
                res.append(int(_))
        return res

    res_list = []
    for _ in in_str.splitlines():
        piece_list = _.split(" ")
        operation_name = piece_list[0]
        registers = proc_registers(piece_list[1:])
        res_list.append((operation_name, registers))
    return res_list


def proc_input(in_data):
    """
    retuces the input into block decrribed by 3 numbers each
    """

    def split_data(in_data):
        res_list = []
        cur_block = [in_data[0]]
        for _ in in_data[1:]:
            if _[0] == "inp":
                res_list.append(cur_block)
                cur_block = [_]

            else:
                cur_block.append(_)
        res_list.append(cur_block)
        return res_list

    def proc_block_to_num(in_block):
        assert in_block[4][0] == "div"
        assert in_block[4][1][0] == "z"
        assert isinstance(in_block[4][1][1], int)
        val_a = in_block[4][1][1]
        assert val_a in {1, 26}

        assert in_block[5][0] == "add"
        assert in_block[5][1][0] == "x"
        assert isinstance(in_block[5][1][1], int)
        val_b = in_block[5][1][1]

        assert in_block[-3][0] == "add"
        assert in_block[-3][1][0] == "y"
        assert isinstance(in_block[-3][1][1], int)
        val_c = in_block[-3][1][1]
        return val_a, val_b, val_c

    blocks = split_data(in_data)
    return tuple(proc_block_to_num(_) for _ in blocks)


def compute(in_block, in_z, in_w):
    """
    returns the value in the z register after computng the in_block
    for given in_z and in_w
    """
    tmp_x = in_block[1] + (in_z % 26)
    out_z = in_z // in_block[0]
    if tmp_x != in_w:
        out_z *= 26
        out_z += in_w + in_block[2]
    return out_z


@functools.lru_cache(None)
def find_all_versions(in_blocks):
    """returns the sorted list of all verons (i.e. valid inputs)"""

    def get_z_limit_list(in_block_num_data):
        res = [26]
        for _ in reversed(in_block_num_data[:-1]):
            res.append(res[-1] * _[0])
        return res[::-1]

    z_limits = get_z_limit_list(in_blocks)

    @functools.lru_cache(None)
    def inner(cur_pos, in_z):
        if cur_pos >= len(in_blocks):
            res = [""] if in_z == 0 else []
        elif in_z > z_limits[cur_pos]:
            res = []
        else:
            tmp_x = in_blocks[cur_pos][1] + in_z % 26
            w_range = list(range(1, 10))
            if 1 <= tmp_x <= 9:
                w_range = [tmp_x]
            res = []
            for cur_w in w_range:
                znext = compute(in_blocks[cur_pos], in_z, cur_w)
                new_res = inner(cur_pos + 1, znext)
                for _ in new_res:
                    res.append(str(cur_w) + _)
        return res

    res = [int(_) for _ in inner(0, 0)]
    assert all(res[_] < res[_ + 1] for _ in range(len(res) - 1))
    return res


def solve_a(in_str):
    """solution function for part a"""
    return find_all_versions(proc_input(parse_input(in_str)))[-1]


def solve_b(in_str):
    """solution function for part b"""
    return find_all_versions(proc_input(parse_input(in_str)))[0]
