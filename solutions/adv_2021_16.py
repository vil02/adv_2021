"""
solution of adv_2021_16
"""
import functools


def parse_input(in_str):
    """parses the input hex string into a string of 0's and 1's"""

    def proc_single(in_char):
        res = bin(int(in_char, 16))
        assert res.startswith("0b")
        res = res[2:]
        if len(res) < 4:
            res = "0" * (4 - len(res)) + res
        return res

    return "".join(proc_single(_) for _ in in_str.strip())


def bin_to_int(in_str):
    """returns the integer value represented by the binnary string in_str"""
    return int(in_str, 2)


def read_header(in_data):
    """reads the version and the packet_id"""
    version = bin_to_int("".join(in_data[0:3]))
    packet_id = bin_to_int("".join(in_data[3:6]))
    rem_data = "".join(in_data[6:])
    return version, packet_id, rem_data


def read_literal(in_data):
    """reads the literal from the begining of the in_data"""

    def read_block(in_tmp_data):
        continue_reading = False
        res = continue_reading, None, in_tmp_data
        if len(in_tmp_data) >= 5:
            if in_tmp_data[0] == "1":
                continue_reading = True
            value = "".join(in_tmp_data[1:5])
            res = continue_reading, value, in_tmp_data[5:]
        return res

    literal_data = []
    continue_reading, cur_val, tmp_data = read_block(in_data)
    literal_data.append(cur_val)
    while continue_reading:
        continue_reading, cur_val, tmp_data = read_block(tmp_data)
        literal_data.append(cur_val)
    return bin_to_int("".join(literal_data)), tmp_data


def read_operator(in_data):
    """reads the operator from the beginning of the in_data"""
    len_id = in_data[0]
    tmp_data = in_data[1:]
    if len_id == "0":
        total_len = bin_to_int("".join(tmp_data[:15]))
        tmp_data = tmp_data[15:]
        bits_read = 0
        res_data = []
        while bits_read < total_len:
            org_len = len(tmp_data)
            tmp_res_data, tmp_data = read_data(tmp_data)
            res_data.append(tmp_res_data)
            bits_read += org_len - len(tmp_data)
    else:
        assert len_id == "1"
        number_of_blocks = bin_to_int("".join(tmp_data[:11]))
        tmp_data = tmp_data[11:]
        res_data = []
        for _ in range(number_of_blocks):
            tmp_res_data, tmp_data = read_data(tmp_data)
            res_data.append(tmp_res_data)
    return res_data, tmp_data


def read_data(in_data):
    """parses the in_data into a dicitonary"""
    assert set(list(in_data)).issubset({"0", "1"})
    tmp_data = "".join(in_data)
    res_data = {}
    if len(tmp_data) > 6:
        cur_version, cur_id, tmp_data = read_header(tmp_data)
        if cur_id == 4:
            literal_value, tmp_data = read_literal(tmp_data)
            res_data = {
                "version": cur_version,
                "id": cur_id,
                "value": literal_value,
            }
        else:
            operator_data, tmp_data = read_operator(tmp_data)
            res_data = {
                "version": cur_version,
                "id": cur_id,
                "operator_data": operator_data,
            }
    return res_data, "".join(tmp_data)


def get_version_sum(in_data):
    """
    returns the sum of the values with the key 'version' stored in in_data
    """
    assert "version" in in_data
    res = in_data["version"]
    if "operator_data" in in_data:
        res += sum(get_version_sum(_) for _ in in_data["operator_data"])
    return res


def solve_a(in_str):
    """solution function for part a"""
    data, _ = read_data(parse_input(in_str))
    return get_version_sum(data)


def evaluate(in_data):
    """
    evaluates the in_data as described in part_b
    """

    def greater_fun(in_num_list):
        assert len(in_num_list) == 2
        return 1 if in_num_list[0] > in_num_list[1] else 0

    def less_fun(in_num_list):
        return greater_fun(in_num_list[::-1])

    def equal_fun(in_num_list):
        assert len(in_num_list) == 2
        return 1 if in_num_list[0] == in_num_list[1] else 0

    def prod_fun(in_num_list):
        return functools.reduce(lambda a, b: a * b, in_num_list)

    assert "id" in in_data
    cur_id = in_data["id"]
    if cur_id == 4:
        res = in_data["value"]
    else:
        fun_dict = {
            0: sum,
            1: prod_fun,
            2: min,
            3: max,
            5: greater_fun,
            6: less_fun,
            7: equal_fun,
        }
        res = fun_dict[cur_id]([evaluate(_) for _ in in_data["operator_data"]])
    return res


def solve_b(in_str):
    """solution function for part b"""
    data, _ = read_data(parse_input(in_str))
    return evaluate(data)
