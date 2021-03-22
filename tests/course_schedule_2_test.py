from problems.course_schedule_2 import find_order
from test_utils import compare_lists


def test_course_schedule_2_1():
    num_courses = 2
    pre_reqs = [[1, 0]]
    expected = [0, 1]
    actual = find_order(num_courses, pre_reqs)
    assert compare_lists(actual, expected) is True


def test_course_schedule_2_2():
    num_courses = 4
    pre_reqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
    expected = [0, 2, 1, 3]
    actual = find_order(num_courses, pre_reqs)
    assert compare_lists(actual, expected) is True


def test_course_schedule_2_3():
    num_courses = 1
    pre_reqs = []
    expected = [0]
    actual = find_order(num_courses, pre_reqs)
    assert compare_lists(actual, expected) is True
