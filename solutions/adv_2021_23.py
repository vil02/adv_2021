"""
solution of adv_2021_23
"""
import functools
import math


def parse_input(in_str):
    """
    Parses the input into rooms.
    Object at index 0 is the deepest.
    """
    char_list = [_ for _ in in_str if _ in {'A', 'B', 'C', 'D'}]
    assert len(char_list) == 8
    room_a = [char_list[0], char_list[4]]
    room_b = [char_list[1], char_list[5]]
    room_c = [char_list[2], char_list[6]]
    room_d = [char_list[3], char_list[7]]
    return room_a, room_b, room_c, room_d


def _joint_pos_dict():
    return {'A': 2, 'B': 4, 'C': 6, 'D': 8}


def _empty_corridor():
    return tuple('' for _ in range(11))


def calculate_move_length(in_room_name, in_room_index, in_end_pos):
    assert in_end_pos not in _joint_pos_dict().values()
    vert_part = 1+in_room_index
    horz_part = abs(_joint_pos_dict()[in_room_name]-in_end_pos)
    return vert_part+horz_part


def is_move_possible(in_room_name, in_end_pos, in_corridor):
    def get_search_range(in_pos_a, in_pos_b):
        return range(min(in_pos_a, in_pos_b), max(in_pos_a, in_pos_b)+1)
    assert len(in_corridor) == len(_empty_corridor())
    joint_pos = _joint_pos_dict()[in_room_name]
    return all(in_corridor[_] == ''
               for _ in get_search_range(joint_pos, in_end_pos))


def calculate_move_cost(in_name, in_len):
    single_move_cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    return single_move_cost[in_name]*in_len


def _get_room_name(in_room_id):
    return {0: 'A', 1: 'B', 2: 'C', 3: 'D'}[in_room_id]


def _is_room_done(in_room_id, in_room_data):
    return all(_ == _get_room_name(in_room_id) for _ in in_room_data)

def _is_room_empty(in_room):
    return all(_ == '' for _ in in_room)


def _get_all_moves_from_room(in_room_id, in_corridor):
    room_name = _get_room_name(in_room_id)
    return [_ for _ in range(len(in_corridor))
            if is_move_possible(room_name, _, in_corridor)]


#def make_move_from_room(in_rooms, in_corridor, in_room_id, in_end_pos):
#    def move_out_from_the_room(in_room):
#        new_room = list(in_room):
#
#    assert in_corridor[in_end_pos] == ''
#    new_rooms = copy.deepcopy(in_rooms)



@functools.lru_cache(None)
def find_min_cost(in_rooms, in_corridor=_empty_corridor()):
    if all(_is_room_done(*_) for _ in enumerate(in_rooms)):
        assert all(_ == '' for _ in in_corridor)
        res = 0
    else:
        cur_res = math.inf
        for (room_id, room_data) in enumerate(in_rooms):
            if not _is_room_done(room_id, room_data) and not _is_room_empty(in_rooms[room_id]):
                for end_pos in _get_all_moves_from_room(room_id, in_corridor):
                    pass



    return res

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
