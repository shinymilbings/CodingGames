from AdventOfCode2020.lib import rw
import re


def validate_hgt(height):
    if height[-2:] == 'in':
        if 59 <= int(height[:-2]) <= 76:
            return True
    elif height[-2:] == 'cm':
        if 150 <= int(height[:-2]) <= 193:
            return True
    else:
        return False


def validate_passport(passport, required_fields, strict=False):
    if len([x for x in required_fields if x not in passport.keys()]) == 0:
        if strict:
            if 1920 <= int(passport['byr']) <= 2002 and \
                    2010 <= int(passport['iyr']) <= 2020 and \
                    2020 <= int(passport['eyr']) <= 2030 and \
                    validate_hgt(height=passport['hgt']) and \
                    re.match(r'#[0-9a-f]{6}$', passport['hcl']) and \
                    re.match(r'(amb|blu|brn|gry|grn|hzl|oth)$', passport['ecl']) and \
                    re.match(r'\d{9}$', passport['pid']):
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def parse_input_contents(puzzle_input):
    parsed_list = []
    passport_dict = {}
    for line in puzzle_input:
        if line == '\n':
            parsed_list.append(dict(passport_dict))
            passport_dict = {}
        else:
            for i in line.replace('\n', '').split(' '):
                passport_dict[i.split(':')[0]] = i.split(':')[1]
    parsed_list.append(dict(passport_dict))
    print(parsed_list[-1])
    return parsed_list


if __name__ == '__main__':
    raw_input = rw.get_contents(script_path=__file__)
    nice_input = parse_input_contents(puzzle_input=raw_input)
    required_passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    rw.write_output(script_path=__file__, part='1',
                    solution=len([x for x in nice_input if validate_passport(passport=x,
                                                                             required_fields=required_passport_fields)]))
    rw.write_output(script_path=__file__, part='2',
                    solution=len([x for x in nice_input if validate_passport(passport=x,
                                                                             required_fields=required_passport_fields,
                                                                             strict=True)]))
