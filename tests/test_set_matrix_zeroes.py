from problems.set_matrix_zeroes import set_zeroes
from test_utils import compare_lists


def test_set_matrix_zeroes_1():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    set_zeroes(matrix)
    assert len(expected) == len(matrix)
    for i in range(len(matrix)):
        assert compare_lists(expected[i], matrix[i]) is True


def test_set_matrix_zeroes_2():
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    set_zeroes(matrix)
    assert len(expected) == len(matrix)
    for i in range(len(matrix)):
        assert compare_lists(expected[i], matrix[i]) is True


def test_set_matrix_zeroes_3():
    matrix = [[1, 0]]
    expected = [[0, 0]]
    set_zeroes(matrix)
    assert len(expected) == len(matrix)
    for i in range(len(matrix)):
        assert compare_lists(expected[i], matrix[i]) is True


def test_set_matrix_zeroes_4():
    matrix = [[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 0, 0, 1]]
    expected = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    set_zeroes(matrix)
    assert len(expected) == len(matrix)
    for i in range(len(matrix)):
        assert compare_lists(expected[i], matrix[i]) is True
