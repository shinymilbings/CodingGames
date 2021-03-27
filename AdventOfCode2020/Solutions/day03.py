from AdventOfCode2020.lib import rw


def parse_input_contents(puzzle_input):
    return [x.replace('\n', '') for x in puzzle_input]


def count_trees_in_path(slope_pattern, slope_map):
    x_pos, y_pos = 0, 0
    tree_count = 0
    x_increment, y_increment = slope_pattern
    while y_pos < len(slope_map):
        if slope_map[y_pos][x_pos] == '#':
            tree_count += 1
        x_pos = (x_pos + x_increment) % len(slope_map[0])
        y_pos = y_pos + y_increment
    return tree_count


def multiply_slope_tree_counts(slope_patterns, slope_map):
    tree_count = 1
    for s in slope_patterns:
        tree_count = tree_count * count_trees_in_path(slope_pattern=s, slope_map=slope_map)
    return tree_count


if __name__ == '__main__':
    raw_input = rw.get_contents(script_path=__file__)
    nice_input = parse_input_contents(puzzle_input=raw_input)
    rw.write_output(script_path=__file__, part='1',
                    solution=(count_trees_in_path(slope_pattern=[3, 1], slope_map=nice_input)))
    rw.write_output(script_path=__file__, part='2',
                    solution=(multiply_slope_tree_counts(slope_patterns=[[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]],
                                                         slope_map=nice_input)))

