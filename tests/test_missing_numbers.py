from problems.missing_numbers import missing_number


def test_missing_number_1():
    nums = [3, 0, 1]
    expected = 2
    actual = missing_number(nums)
    assert actual == expected


def test_missing_number_2():
    nums = [0, 1]
    expected = 2
    actual = missing_number(nums)
    assert actual == expected


def test_missing_number_3():
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    expected = 8
    actual = missing_number(nums)
    assert actual == expected


def test_missing_number_4():
    nums = [0]
    expected = 1
    actual = missing_number(nums)
    assert actual == expected
