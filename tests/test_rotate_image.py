from problems.rotate_image import rotate
from test_utils import compare_lists


def test_rotate_image_1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    rotate(matrix)
    assert len(matrix) == len(expected)
    for i in range(len(matrix)):
        assert compare_lists(expected[i], matrix[i]) is True


def test_rotate_image_2():
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    expected = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    rotate(matrix)
    assert len(matrix) == len(expected)
    for i in range(len(matrix)):
        assert compare_lists(expected[i], matrix[i]) is True


def test_rotate_image_3():
    matrix = [[1]]
    expected = [[1]]
    rotate(matrix)
    assert len(matrix) == len(expected)
    for i in range(len(matrix)):
        assert compare_lists(expected[i], matrix[i]) is True


def test_rotate_image_4():
    matrix = [[1, 2], [3, 4]]
    expected = [[3, 1], [4, 2]]
    rotate(matrix)
    assert len(matrix) == len(expected)
    for i in range(len(matrix)):
        assert compare_lists(expected[i], matrix[i]) is True
