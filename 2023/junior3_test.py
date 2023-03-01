from junior3 import get_maximum_participants

def test_case_1():
    availabilities = [
        "YY.Y.",
        "...Y.",
        ".YYY."
    ]
    assert get_maximum_participants(availabilities) == "4"

def test_case_2():
    availabilities = [
        "YY..Y",
        ".YY.Y",
        ".Y.Y.",
        ".YY.Y",
        "Y...Y",
    ]
    assert get_maximum_participants(availabilities) == "2,5"