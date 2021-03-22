from typing import List

from problems.two_sum import two_sum


def test_two_sum_1():
    nums: List = [2, 7, 11, 15]
    target: int = 9
    expected: List = [0, 1]
    actual: List = two_sum(nums, target)
    assert actual == expected


def test_two_sum_2():
    nums: List = [3, 2, 4]
    target: int = 6
    expected: List = [1, 2]
    actual: List = two_sum(nums, target)
    assert actual == expected


def test_two_sum_3():
    nums: List = [3, 3]
    target: int = 6
    expected: List = [0, 1]
    actual: List = two_sum(nums, target)
    assert actual == expected
