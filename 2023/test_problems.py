from unittest import TestCase
from test_utility import execute_test_cases

from j1 import get_final_score
from j2 import calculate_total_spiciness


class Test(TestCase):
    def test_j1(self):
        execute_test_cases("j1", get_final_score)

    def test_j2(self):
        execute_test_cases("j2", calculate_total_spiciness)
