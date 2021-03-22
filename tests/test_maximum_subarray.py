from problems.maximum_subarray import max_subarray


def test_maximum_subarray_1():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 6
    actual = max_subarray(nums)
    assert actual == expected


def test_maximum_subarray_2():
    nums = [1]
    expected = 1
    actual = max_subarray(nums)
    assert actual == expected


def test_maximum_subarray_3():
    nums = [5, 4, -1, 7, 8]
    expected = 23
    actual = max_subarray(nums)
    assert actual == expected
