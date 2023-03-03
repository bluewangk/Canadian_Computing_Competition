import os

TEST_DATA_DIR = os.path.join(os.path.realpath(os.path.dirname(__file__)), "test_data")
IN_SUFFIX = ".in"
OUT_SUFFIX = ".out"

def execute_test_cases(problem, func):
    cases_dir = os.path.join(TEST_DATA_DIR, problem)
    os.chdir(cases_dir)
    for input_file in os.listdir(cases_dir):
        if input_file.endswith(IN_SUFFIX):
            case_name = input_file.removesuffix(IN_SUFFIX)
            output_file = case_name + OUT_SUFFIX
            inputs = open(input_file).read()
            output = open(output_file).read()

            assert func(inputs) == str(output).rstrip()

def test_j1_cases():
    from j1 import get_final_score
    execute_test_cases("j1", get_final_score)