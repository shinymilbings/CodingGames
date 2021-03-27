from AdventOfCode2020.lib import rw


def parse_input_contents(puzzle_input):
    return [int(x.replace('\n', '')) for x in puzzle_input]


def part01_solver(puzzle_input):
    for x in puzzle_input:
        for y in puzzle_input:
            if x + y == 2020 and x != y:
                return x * y


def part02_solver(puzzle_input):
    for x in puzzle_input:
        for y in puzzle_input:
            for z in puzzle_input:
                if x + y + z == 2020 and x != y and x != z and y != z:
                    return x * y * z


if __name__ == '__main__':
    raw_input = rw.get_contents(script_path=__file__)
    nice_input = parse_input_contents(puzzle_input=raw_input)
    rw.write_output(script_path=__file__, part='1', solution=part01_solver(puzzle_input=nice_input))
    rw.write_output(script_path=__file__, part='2', solution=part02_solver(puzzle_input=nice_input))
