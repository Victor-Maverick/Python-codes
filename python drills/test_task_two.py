import task_two
import pytest


class TestListFunction:
    def test_that_function_is_not_none(self):
        sample_list = list(range(10, 20))
        assert 10 == task_two.get_length(sample_list);

    def test_for_even_position_sum(self):
        sample_list = list(range(10, 20))
        assert 70 == task_two.get_even_sum(sample_list);


    def test_for_odd_position_sum(self):
        sample_list = list(range(10, 20))
        assert 75 == task_two.get_odd_sum(sample_list);