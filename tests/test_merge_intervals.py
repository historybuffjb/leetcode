from problems.merge_intervals import merge


def test_merge_intervals_1():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected = [[1, 6], [8, 10], [15, 18]]
    actual = merge(intervals)
    assert actual == expected


def test_merge_intervals_2():
    intervals = [[1, 4], [4, 5]]
    expected = [[1, 5]]
    actual = merge(intervals)
    assert actual == expected


def test_merge_intervals_3():
    intervals = [[1, 30], [3, 6], [9, 12], [18, 29]]
    expected = [[1, 30]]
    actual = merge(intervals)
    assert actual == expected


def test_merge_intervals_4():
    intervals = [[1, 9], [2, 5], [19, 20], [10, 11], [12, 20], [0, 3], [0, 1], [0, 2]]
    expected = [[0, 9], [10, 11], [12, 20]]
    actual = merge(intervals)
    assert actual == expected
