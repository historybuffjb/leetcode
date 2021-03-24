from problems.maximum_length_of_repeated_subarray import find_length


def test_maximum_length_of_repeated_subarray_1():
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 1, 4, 7]
    expected = 3
    actual = find_length(a, b)
    assert actual == expected


def test_maximum_length_of_repeated_subarray_2():
    a = [0]
    b = [3, 2, 1, 4, 7]
    expected = 0
    actual = find_length(a, b)
    assert actual == expected


def test_maximum_length_of_repeated_subarray_3():
    a = [1]
    b = [3, 2, 1, 4, 7]
    expected = 1
    actual = find_length(a, b)
    assert actual == expected


def test_maximum_length_of_repeated_subarray_4():
    a = [1, 2, 3]
    b = [1, 2, 3]
    expected = 3
    actual = find_length(a, b)
    assert actual == expected
