from problem_4 import calculate_tape_length

def test_case_1():
    assert calculate_tape_length(5, "1 0 1 0 1", "0 0 0 0 0") == 9

def test_case_2():
    assert calculate_tape_length(7, "0 0 1 1 0 1 0", "0 0 1 0 1 0 0") == 11