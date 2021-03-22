from problems.peak_index_in_a_mountain_array import peak_index_in_mountain_array


def test_peak_index_in_a_mountain_array_1():
    arr = [0, 1, 0]
    expected = 1
    actual = peak_index_in_mountain_array(arr)
    assert actual == expected


def test_peak_index_in_a_mountain_array_2():
    arr = [0, 2, 1, 0]
    expected = 1
    actual = peak_index_in_mountain_array(arr)
    assert actual == expected


def test_peak_index_in_a_mountain_array_3():
    arr = [0, 10, 5, 2]
    expected = 1
    actual = peak_index_in_mountain_array(arr)
    assert actual == expected


def test_peak_index_in_a_mountain_array_4():
    arr = [3, 4, 5, 1]
    expected = 2
    actual = peak_index_in_mountain_array(arr)
    assert actual == expected


def test_peak_index_in_a_mountain_array_5():
    arr = [24, 69, 100, 99, 79, 78, 36, 26, 19]
    expected = 2
    actual = peak_index_in_mountain_array(arr)
    assert actual == expected
