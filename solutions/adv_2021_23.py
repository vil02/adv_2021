"""
solution of adv_2021_23
"""


def parse_input(in_str):
    char_list = [_ for _ in in_str if _ in {'A', 'B', 'C', 'D'}]
    assert len(char_list) == 8
    room_a = [char_list[0], char_list[4]]
    room_b = [char_list[1], char_list[5]]
    room_c = [char_list[2], char_list[6]]
    room_d = [char_list[3], char_list[7]]
    return room_a, room_b, room_c, room_d

# def solve_a(in_str):
#     """solution function for part a"""
#     pass
#
#
# def solve_b(in_str):
#     """solution function for part b"""
#     pass
