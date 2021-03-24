from problems.majority_element import majority_element


def test_majority_element_1():
    nums = [3, 2, 3]
    expected = 3
    actual = majority_element(nums)
    assert actual == expected


def test_majority_element_2():
    nums = [2, 2, 1, 1, 1, 2, 2]
    expected = 2
    actual = majority_element(nums)
    assert actual == expected


def test_majority_element_3():
    nums = [1]
    expected = 1
    actual = majority_element(nums)
    assert actual == expected


def test_majority_element_4():
    nums = [1, 1, 2]
    expected = 1
    actual = majority_element(nums)
    assert actual == expected


def test_majority_element_5():
    nums = [-7, 2, -7, 3, -7, 6, -7, -7, 9, 10, -7]
    expected = -7
    actual = majority_element(nums)
    assert actual == expected
