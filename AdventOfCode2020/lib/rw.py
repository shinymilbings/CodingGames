import os


def write_output(script_path, part, solution):
    basedir = os.path.dirname(script_path)
    basedir = basedir.replace('Solutions', 'outputs')
    day = os.path.basename(script_path).replace('.py', '')
    solution_file = day + '_' + part + '_' + '.txt'
    output_file_path = os.path.join(basedir, solution_file)
    with open(file=output_file_path, mode='w') as f:
        print(solution, file=f)
        f.close()


def get_contents(script_path):
    basedir = os.path.dirname(script_path)
    basedir = basedir.replace('Solutions', 'inputs')
    day = os.path.basename(script_path).replace('.py', '.txt')
    input_file_path = os.path.join(basedir, day)
    with open(input_file_path) as f:
        input_contents = f.readlines()
        f.close()
    return input_contents
