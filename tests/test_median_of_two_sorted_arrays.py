from problems.median_of_two_sorted_arrays import find_median_sorted_array


def test_median_of_two_sorted_arrays_1():
    nums1 = [1, 3]
    nums2 = [2]
    expected = 2.0
    actual = find_median_sorted_array(nums1, nums2)
    assert actual == expected


def test_median_of_two_sorted_arrays_2():
    nums1 = [1, 2]
    nums2 = [3, 4]
    expected = 2.5
    actual = find_median_sorted_array(nums1, nums2)
    assert actual == expected


def test_median_of_two_sorted_arrays_3():
    nums1 = [0, 0]
    nums2 = [0, 0]
    expected = 0.0
    actual = find_median_sorted_array(nums1, nums2)
    assert actual == expected


def test_median_of_two_sorted_arrays_4():
    nums1 = []
    nums2 = [1]
    expected = 1.0
    actual = find_median_sorted_array(nums1, nums2)
    assert actual == expected


def test_median_of_two_sorted_arrays_5():
    nums1 = [2]
    nums2 = []
    expected = 2.0
    actual = find_median_sorted_array(nums1, nums2)
    assert actual == expected


def test_median_of_two_sorted_arrays_6():
    nums1 = [1, 12, 15, 26, 38]
    nums2 = [2, 13, 17, 30, 45]
    expected = 16.0
    actual = find_median_sorted_array(nums1, nums2)
    assert actual == expected


def test_median_of_two_sorted_arrays_7():
    nums1 = [1, 12, 15, 26, 38]
    nums2 = [2, 13, 17, 30, 45]
    expected = 16.0
    actual = find_median_sorted_array(nums1, nums2)
    assert actual == expected


def test_median_of_two_sorted_arrays_8():
    nums1 = [-5, 3, 6, 12, 15]
    nums2 = [-12, -10, -6, -3, 4, 10]
    expected = 3.0
    actual = find_median_sorted_array(nums1, nums2)
    assert actual == expected


def test_median_of_two_sorted_arrays_9():
    nums1 = [2, 3, 5, 8]
    nums2 = [10, 12, 14, 16, 18, 20]
    expected = 11.0
    actual = find_median_sorted_array(nums1, nums2)
    assert actual == expected


def test_median_of_two_sorted_arrays_10():
    nums1 = [2, 3, 5, 8]
    nums2 = [10, 12, 14, 16, 18, 20]
    expected = 11.0
    actual = find_median_sorted_array(nums1, nums2)
    assert actual == expected


def test_median_of_two_sorted_arrays_11():
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nums2 = [11, 12, 13, 14, 15, 16, 17, 18, 19]
    expected = 10.0
    actual = find_median_sorted_array(nums1, nums2)
    assert actual == expected
