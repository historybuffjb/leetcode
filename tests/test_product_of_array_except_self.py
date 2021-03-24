from problems.product_of_array_except_self import product_except_self
from test_utils import compare_lists

DEBUG = False


def test_product_of_array_except_self_1():
    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]
    actual = product_except_self(nums)
    assert compare_lists(expected, actual, DEBUG) is True


def test_product_of_array_except_self_2():
    nums = [-1, 1, 0, -3, 3]
    expected = [0, 0, 9, 0, 0]
    actual = product_except_self(nums)
    assert compare_lists(expected, actual, DEBUG) is True


def test_product_of_array_except_self_3():
    nums = [1, -1]
    expected = [-1, 1]
    actual = product_except_self(nums)
    assert compare_lists(expected, actual, DEBUG) is True


def test_product_of_array_except_self_4():
    nums = [1, 2, 3]
    expected = [6, 3, 2]
    actual = product_except_self(nums)
    assert compare_lists(expected, actual, DEBUG) is True


def test_product_of_array_except_self_5():
    nums = [1, 0]
    expected = [0, 1]
    actual = product_except_self(nums)
    assert compare_lists(expected, actual, DEBUG) is True
