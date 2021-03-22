from problems.squares_of_a_sorted_array import sorted_squares
from test_utils import compare_lists

DEBUG = False


def test_squares_of_a_sorted_array_1():
    nums = [-4, -1, 0, 3, 10]
    expected = [0, 1, 9, 16, 100]
    actual = sorted_squares(nums)
    assert compare_lists(expected, actual, DEBUG) is True


def test_squares_of_a_sorted_array_2():
    nums = [-7, -3, 2, 3, 11]
    expected = [4, 9, 9, 49, 121]
    actual = sorted_squares(nums)
    assert compare_lists(expected, actual, DEBUG) is True


def test_squares_of_a_sorted_array_3():
    nums = [2]
    expected = [4]
    actual = sorted_squares(nums)
    assert compare_lists(expected, actual, DEBUG) is True


def test_squares_of_a_sorted_array_4():
    nums = [-15]
    expected = [225]
    actual = sorted_squares(nums)
    assert compare_lists(expected, actual, DEBUG) is True


def test_squares_of_a_sorted_array_5():
    nums = [0]
    expected = [0]
    actual = sorted_squares(nums)
    assert compare_lists(expected, actual, DEBUG) is True
