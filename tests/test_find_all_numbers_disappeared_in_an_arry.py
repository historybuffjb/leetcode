from problems.find_all_numbers_disappeared_in_an_arry import find_disappeared_number


def test_find_all_numbers_disappeared_in_an_array_1():
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    expected = [5, 6]
    actual = find_disappeared_number(nums)
    assert actual == expected


def test_find_all_numbers_disappeared_in_an_array_2():
    nums = [1]
    expected = []
    actual = find_disappeared_number(nums)
    assert actual == expected


def test_find_all_numbers_disappeared_in_an_array_3():
    nums = [1, 1, 1]
    expected = [2, 3]
    actual = find_disappeared_number(nums)
    assert actual == expected


def test_find_all_numbers_disappeared_in_an_array_4():
    nums = [2, 2]
    expected = [1]
    actual = find_disappeared_number(nums)
    assert actual == expected
