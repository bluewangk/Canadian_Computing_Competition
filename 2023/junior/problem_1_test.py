from problem_1 import get_final_score


def test_case_1():
    assert get_final_score(5, 2) == 730

def test_case_2():
    assert get_final_score(0, 10) == -100