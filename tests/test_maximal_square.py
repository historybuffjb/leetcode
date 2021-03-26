from problems.maximal_square import maximal_square


def test_maximal_square_1():
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    expected = 4
    actual = maximal_square(matrix)
    assert actual == expected


def test_maximal_square_2():
    matrix = [["0", "1"], ["1", "0"]]
    expected = 1
    actual = maximal_square(matrix)
    assert actual == expected


def test_maximal_square_3():
    matrix = [
        ["0", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "1"],
        ["0", "1", "1", "1", "1"],
        ["0", "1", "1", "1", "1"],
        ["0", "0", "1", "1", "1"],
    ]
    expected = 9
    actual = maximal_square(matrix)
    assert actual == expected


def test_maximal_square_4():
    matrix = [
        ["0", "1", "1", "0", "1"],
        ["1", "1", "0", "1", "0"],
        ["0", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "1"],
        ["0", "0", "0", "0", "0"],
    ]
    expected = 9
    actual = maximal_square(matrix)
    assert actual == expected
