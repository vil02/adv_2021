"""
solution of adv_2021_23
"""


def parse_input(in_str):
    """
    Parses the input into rooms.
    Object at index 0 is the deepest.
    """
    char_list = [_ for _ in in_str if _ in {'A', 'B', 'C', 'D'}]
    assert len(char_list) == 8
    room_a = [char_list[4], char_list[0]]
    room_b = [char_list[5], char_list[1]]
    room_c = [char_list[6], char_list[2]]
    room_d = [char_list[7], char_list[3]]
    return room_a, room_b, room_c, room_d


def calculate_move_length(in_room_name, in_room_index, in_end_pos):
    joint_pos_dict = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
    assert in_end_pos not in joint_pos_dict.values()
    vert_part = 4-in_room_index
    horz_part = abs(joint_pos_dict[in_room_name]-in_end_pos)
    return vert_part+horz_part
#
#def get_cost_():
#    """returns the dictionary """
#    return {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

# def solve_a(in_str):
#     """solution function for part a"""
#     pass
#
#
# def solve_b(in_str):
#     """solution function for part b"""
#     pass
