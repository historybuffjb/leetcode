from problems.find_all_duplicates_in_an_array import find_duplicates
from test_utils import compare_lists

DEBUG = False


def test_find_all_duplicates_in_an_array_1():
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    expected = [2, 3]
    actual = find_duplicates(nums)
    assert compare_lists(expected, actual, DEBUG) is True


def test_find_all_duplicates_in_an_array_2():
    nums = [1, 1]
    expected = [1]
    actual = find_duplicates(nums)
    assert compare_lists(expected, actual, DEBUG) is True


def test_find_all_duplicates_in_an_array_3():
    nums = [1, 2, 3, 2]
    expected = [2]
    actual = find_duplicates(nums)
    assert compare_lists(expected, actual, DEBUG) is True


def test_find_all_duplicates_in_an_array_4():
    nums = [1, 4, 5, 6, 9, 3, 4, 5, 1, 6]
    expected = [4, 5, 1, 6]
    actual = find_duplicates(nums)
    assert compare_lists(expected, actual, DEBUG) is True
