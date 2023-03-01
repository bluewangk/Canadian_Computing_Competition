from junior2 import calculate_total_speciness

def test_case_1():
    assert calculate_total_speciness(["Poblano", "Cayenne", "Thai", "Poblano"]) == 118000

def test_case_2():
    assert calculate_total_speciness(["Poblano", "None"]) == 1500