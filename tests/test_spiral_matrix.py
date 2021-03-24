from problems.spiral_matrix import spiral_order
from test_utils import compare_lists


def test_spiral_matrix_1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    actual = spiral_order(matrix)
    assert compare_lists(expected, actual) is True


def test_spiral_matrix_2():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    actual = spiral_order(matrix)
    assert compare_lists(expected, actual) is True


def test_spiral_matrix_3():
    matrix = [[1, 2, 3, 4]]
    expected = [1, 2, 3, 4]
    actual = spiral_order(matrix)
    assert compare_lists(expected, actual) is True


def test_spiral_matrix_4():
    matrix = [[1]]
    expected = [1]
    actual = spiral_order(matrix)
    assert compare_lists(expected, actual) is True


def test_spiral_matrix_5():
    matrix = [[1, 2]]
    expected = [1, 2]
    actual = spiral_order(matrix)
    assert compare_lists(expected, actual) is True


def test_spiral_matrix_6():
    matrix = [[1], [2]]
    expected = [1, 2]
    actual = spiral_order(matrix)
    assert compare_lists(expected, actual) is True


def test_spiral_matrix_7():
    matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    expected = [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
    actual = spiral_order(matrix)
    assert compare_lists(expected, actual) is True
