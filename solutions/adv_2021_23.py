"""
solution of adv_2021_23
"""
import copy
import heapq
import functools


def parse_input(in_str):
    """
    Parses the input into rooms.
    Object at index 0 is the deepest.
    """
    char_list = [_ for _ in in_str if _ in {'A', 'B', 'C', 'D'}]
    assert len(char_list) == 8
    room_a = (char_list[0], char_list[4])
    room_b = (char_list[1], char_list[5])
    room_c = (char_list[2], char_list[6])
    room_d = (char_list[3], char_list[7])
    return room_a, room_b, room_c, room_d


def _joint_pos_dict():
    return {'A': 2, 'B': 4, 'C': 6, 'D': 8}

def _corridor_len():
    return 11

def _empty_corridor():
    return tuple('' for _ in range(_corridor_len()))


def calculate_move_length(in_room_name, in_room_index, in_end_pos):
    assert in_end_pos not in _joint_pos_dict().values()
    vert_part = 1+in_room_index
    horz_part = abs(_joint_pos_dict()[in_room_name]-in_end_pos)
    return vert_part+horz_part


@functools.lru_cache(None)
def is_move_possible(in_room_name, in_end_pos, in_corridor):
    def get_search_range(in_pos_a, in_pos_b):
        return range(min(in_pos_a, in_pos_b), max(in_pos_a, in_pos_b)+1)
    assert len(in_corridor) == _corridor_len()
    joint_pos = _joint_pos_dict()[in_room_name]
    return all(in_corridor[_] == ''
               for _ in get_search_range(joint_pos, in_end_pos))


def calculate_move_cost(in_name, in_len):
    single_move_cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    return single_move_cost[in_name]*in_len


def _get_room_name(in_room_id):
    return {0: 'A', 1: 'B', 2: 'C', 3: 'D'}[in_room_id]


def _get_room_id(in_room_name):
    res = {'A': 0, 'B': 1, 'C': 2, 'D': 3}[in_room_name]
    assert _get_room_name(res) == in_room_name
    return res


def is_room_done(in_room_id, in_room_data):
    return all(_ == _get_room_name(in_room_id) for _ in in_room_data)


def _is_room_empty(in_room):
    return all(_ == '' for _ in in_room)


def is_room_almost_done(in_room_id, in_room_data):
    cur_room = in_room_data[in_room_id]
    return all(_ in {_get_room_name(in_room_id), ''} for _ in cur_room) \
        and cur_room[0] == ''


def is_starting_room(in_room_id, in_rooms):
    return not is_room_almost_done(in_room_id, in_rooms) \
        and not _is_room_empty(in_rooms[in_room_id]) \
        and not is_room_done(in_room_id, in_rooms[in_room_id])


def _get_all_moves_from_room(in_room_id, in_corridor):
    room_name = _get_room_name(in_room_id)
    return [_ for _ in range(len(in_corridor))
            if is_move_possible(room_name, _, in_corridor)
            and _ not in _joint_pos_dict().values()]


def make_move_from_room(in_rooms, in_corridor, in_room_id, in_end_pos):
    def move_out_from_the_room(in_room):
        assert not _is_room_empty(in_room)
        new_room = list(in_room)
        start_ind = 0
        while new_room[start_ind] == '':
            start_ind += 1
        obj_name = new_room[start_ind]
        new_room[start_ind] = ''
        return tuple(new_room), obj_name, start_ind

    assert in_corridor[in_end_pos] == ''
    assert is_move_possible(
        _get_room_name(in_room_id), in_end_pos, in_corridor)
    new_rooms = list(in_rooms)
    new_corridor = list(in_corridor)

    new_rooms[in_room_id], new_corridor[in_end_pos], start_ind = \
        move_out_from_the_room(new_rooms[in_room_id])

    new_rooms = tuple(new_rooms)
    new_corridor = tuple(new_corridor)

    cost = calculate_move_cost(
        new_corridor[in_end_pos],
        calculate_move_length(
            _get_room_name(in_room_id), start_ind, in_end_pos))
    return new_rooms, new_corridor, cost


def can_go_home(in_name, in_pos, in_corridor, in_room_data):
    def call_is_move_possible():
        tmp_corridor = list(in_corridor)
        tmp_corridor[in_pos] = ''
        return is_move_possible(in_name, in_pos, tuple(tmp_corridor))
    return call_is_move_possible() \
        and is_room_almost_done(_get_room_id(in_name), in_room_data)


def _go_home(in_name, in_pos, in_rooms, in_corridor):
    home_id = _get_room_id(in_name)
    assert is_room_almost_done(home_id, in_rooms)
    assert in_corridor[in_pos] == in_name
    new_corridor = list(in_corridor)
    new_corridor[in_pos] = ''
    new_corridor = tuple(new_corridor)

    room_pos = 0
    while room_pos < len(in_rooms[home_id])-1 \
            and in_rooms[home_id][room_pos+1] == '':
        room_pos += 1

    new_rooms = list(in_rooms)
    new_rooms[home_id] = list(new_rooms[home_id])
    new_rooms[home_id][room_pos] = in_name
    new_rooms[home_id] = tuple(new_rooms[home_id])
    new_rooms = tuple(new_rooms)

    cost = calculate_move_cost(
        in_name,
        calculate_move_length(in_name, room_pos, in_pos))
    return new_rooms, new_corridor, cost


def _is_done(in_rooms):
    return all(is_room_done(*_) for _ in enumerate(in_rooms))


def _gen_new_states(in_cost, in_rooms, in_corridor):
    for room_id in range(len(in_rooms)):
        if is_starting_room(room_id, in_rooms):
            for end_pos in _get_all_moves_from_room(room_id, in_corridor):
                new_rooms, new_corridor, cost = make_move_from_room(
                    in_rooms, in_corridor, room_id, end_pos)
                yield (in_cost+cost, (new_rooms, new_corridor))

    for (obj_pos, obj_name) in enumerate(in_corridor):
        if obj_name != '' and \
                can_go_home(obj_name, obj_pos, in_corridor, in_rooms):
            new_rooms, new_corridor, cost = _go_home(
                obj_name, obj_pos, in_rooms, in_corridor)
            yield (in_cost+cost, (new_rooms, new_corridor))


def find_min_cost(in_rooms):
    known_states = [(0, (in_rooms, _empty_corridor()))]
    visited = set()
    while True:
        cur_cost, (cur_rooms, cur_corridor) = heapq.heappop(known_states)
        if (cur_rooms, cur_corridor) in visited:
            continue
        if _is_done(cur_rooms):
            assert all(_ == '' for _ in cur_corridor)
            return cur_cost
        visited.add((cur_rooms, cur_corridor))
        for _ in _gen_new_states(cur_cost, cur_rooms, cur_corridor):
            heapq.heappush(known_states, _)


def solve_a(in_str):
    """solution function for part a"""
    return find_min_cost(parse_input(in_str))


def extend_data(in_rooms):
    def proc_single_room(in_room, in_ext):
        beg, end = in_room
        assert len(in_ext) == 2
        return beg, in_ext[0], in_ext[1], end
    ext_data = (
        ('D', 'D'),
        ('C', 'B'),
        ('B', 'A'),
        ('A', 'C'))
    return tuple(proc_single_room(*_) for _ in zip(in_rooms, ext_data))


def solve_b(in_str):
    """solution function for part b"""
    return find_min_cost(extend_data(parse_input(in_str)))
