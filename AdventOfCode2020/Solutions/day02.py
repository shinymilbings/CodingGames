from AdventOfCode2020.lib import rw


def parse_input_contents(puzzle_input):
    return [x.replace('\n', '') for x in puzzle_input]


def part1_check_password(password_entry):
    password_requirements, password = [x.strip() for x in password_entry.split(':')]
    char_count, char = password_requirements.split(' ')
    min_chars, max_chars = [int(x) for x in char_count.split('-')]
    if min_chars <= password.count(char) <= max_chars:
        return True
    else:
        return False


def part2_check_password(password_entry):
    password_requirements, password = [x.strip() for x in password_entry.split(':')]
    char_positions, char = password_requirements.split(' ')
    pos_1, pos_2 = [int(x) - 1 for x in char_positions.split('-')]
    if (password[pos_1] == char) ^ (password[pos_2] == char):
        return True
    else:
        return False


if __name__ == '__main__':
    raw_input = rw.get_contents(script_path=__file__)
    nice_input = parse_input_contents(puzzle_input=raw_input)
    rw.write_output(script_path=__file__, part='1',
                    solution=len([x for x in nice_input if part1_check_password(password_entry=x)]))
    rw.write_output(script_path=__file__, part='2',
                    solution=len([x for x in nice_input if part2_check_password(password_entry=x)]))
