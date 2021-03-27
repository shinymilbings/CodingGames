from AdventOfCode2020.lib import rw


def get_seat(input_string):
    row_list = list(range(128))
    column_list = list(range(8))
    for i in range(7):
        if input_string[i] == 'F':
            offset = 0
        else:
            offset = 1
        lower_index = offset * int(len(row_list) / 2)
        upper_index = ((offset + 1) * int(len(row_list) / 2))
        row_list = row_list[lower_index:upper_index]
    row = row_list[0]
    for c in range(7, 10):
        if input_string[c] == "L":
            offset = 0
        else:
            offset = 1
        lower_index = offset * int(len(column_list) / 2)
        upper_index = ((offset + 1) * int(len(column_list) / 2))
        column_list = column_list[lower_index:upper_index]
    column = column_list[0]
    return [row, column]


def get_seat_id(seat):
    return seat[0] * 8 + seat[1]


def get_max_seat_id(ticket_list):
    max_id = 0
    for t in ticket_list:
        s = get_seat(t)
        if max_id < get_seat_id(s):
            max_id = get_seat_id(s)
    return max_id


def find_seat(ticket_list):
    seat_id_list = sorted([get_seat_id(seat=get_seat(input_string=t)) for t in ticket_list])
    for i in range(min(seat_id_list), max(seat_id_list)):
        if (i + 1) in seat_id_list and (i - 1) in seat_id_list and i not in seat_id_list:
            return i


def parse_input_contents(puzzle_input):
    return [x.replace('\n', '') for x in puzzle_input]


if __name__ == '__main__':
    raw_input = rw.get_contents(script_path=__file__)
    nice_input = parse_input_contents(puzzle_input=raw_input)
    rw.write_output(script_path=__file__, part='1', solution=get_max_seat_id(ticket_list=nice_input))
    rw.write_output(script_path=__file__, part='2', solution=find_seat(ticket_list=nice_input))
