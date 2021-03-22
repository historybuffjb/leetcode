from problems.contains_duplicates import contains_duplicates


def test_contains_duplicates_1():
    nums = [1, 2, 3, 1]
    expected = True
    actual = contains_duplicates(nums)
    assert actual == expected


def test_contains_duplicates_2():
    nums = [1, 2, 3, 4]
    expected = False
    actual = contains_duplicates(nums)
    assert actual == expected


def test_contains_duplicates_3():
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    expected = True
    actual = contains_duplicates(nums)
    assert actual == expected


def test_contains_duplicates_4():
    nums = [1]
    expected = False
    actual = contains_duplicates(nums)
    assert actual == expected


def test_contains_duplicates_5():
    nums = [1, 2]
    expected = False
    actual = contains_duplicates(nums)
    assert actual == expected


def test_contains_duplicates_6():
    nums = [1, 1]
    expected = True
    actual = contains_duplicates(nums)
    assert actual == expected


def test_contains_duplicates_7():
    nums = [5, 7, 9, -5, -7, 5]
    expected = True
    actual = contains_duplicates(nums)
    assert actual == expected
