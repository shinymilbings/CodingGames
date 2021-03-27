from AdventOfCode2020.lib import rw


def sum_unique_answers(answer_group):
    return len(set(list(answer_group)))


def get_groups(answer_list):
    answer_groups = []
    a = ''
    for line in answer_list:
        if line == '':
            answer_groups.append(str(a))
            a = ''
        else:
            a += line
    answer_groups.append(a)
    return answer_groups


def sum_all_groups(group_list):
    return sum([sum_unique_answers(g) for g in group_list])


def parse_input_contents(puzzle_input):
    return [x.replace('\n', '') for x in puzzle_input]


if __name__ == '__main__':
    raw_input = rw.get_contents(script_path=__file__)
    nice_input = parse_input_contents(puzzle_input=raw_input)
    rw.write_output(script_path=__file__, part='1', solution=sum_all_groups(
        group_list=get_groups(answer_list=nice_input)))
