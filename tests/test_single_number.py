from problems.single_number import single_number


def test_single_number_1():
    nums = [2, 2, 1]
    expected = 1
    actual = single_number(nums)
    assert actual == expected


def test_single_number_2():
    nums = [4, 1, 2, 1, 2]
    expected = 4
    actual = single_number(nums)
    assert actual == expected


def test_single_number_3():
    nums = [1]
    expected = 1
    actual = single_number(nums)
    assert actual == expected


def test_single_number_4():
    nums = [-6, -3, -6, 5, 5]
    expected = -3
    actual = single_number(nums)
    assert actual == expected


def test_single_number_5():
    nums = [-9, -3, -5, -3, -9]
    expected = -5
    actual = single_number(nums)
    assert actual == expected
