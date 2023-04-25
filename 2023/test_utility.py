import os

TEST_DATA_DIR = os.path.join(os.path.realpath(os.path.dirname(__file__)), "test_data")
IN_SUFFIX = ".in"
OUT_SUFFIX = ".out"


def execute_test_cases(problem, func):
    cases_dir = os.path.join(TEST_DATA_DIR, problem)
    os.chdir(cases_dir)
    for input_file in os.listdir(cases_dir):
        if input_file.endswith(IN_SUFFIX):
            case_name = remove_suffix(input_file, IN_SUFFIX)
            output_file = case_name + OUT_SUFFIX
            with open(input_file) as input_fh, open(output_file) as output_fh:
                inputs = [ipt.rstrip() for ipt in input_fh.readlines()]
                output = output_fh.read()

            expected = str(output).rstrip()
            actual = str(func(inputs))
            print(f'{case_name} expected: {expected}')
            print(f'{case_name} actual: {actual}')
            assert expected == actual


def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string
