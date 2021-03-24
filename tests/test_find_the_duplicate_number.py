from problems.find_the_duplicate_number import find_duplicate


def test_find_the_duplicate_number_1():
    nums = [1, 3, 4, 2, 2]
    expected = 2
    actual = find_duplicate(nums)
    assert actual == expected


def test_find_the_duplicate_number_2():
    nums = [3, 1, 3, 4, 2]
    expected = 3
    actual = find_duplicate(nums)
    assert actual == expected


def test_find_the_duplicate_number_3():
    nums = [1, 1]
    expected = 1
    actual = find_duplicate(nums)
    assert actual == expected


def test_find_the_duplicate_number_4():
    nums = [1, 1, 2]
    expected = 1
    actual = find_duplicate(nums)
    assert actual == expected


def test_find_the_duplicate_number_5():
    nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
    expected = 9
    actual = find_duplicate(nums)
    assert actual == expected
