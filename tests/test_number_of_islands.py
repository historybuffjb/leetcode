from problems.number_of_islands import num_islands


def test_number_of_islands_1():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    expected = 1
    actual = num_islands(grid)
    assert actual == expected


def test_number_of_islands_2():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    expected = 3
    actual = num_islands(grid)
    assert actual == expected


def test_number_of_islands_3():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["0", "1", "0", "0", "1"],
        ["1", "0", "0", "1", "1"],
        ["0", "0", "0", "0", "0"],
        ["1", "0", "1", "0", "1"],
    ]
    expected = 6
    actual = num_islands(grid)
    assert actual == expected


def test_number_of_islands_4():
    grid = [
        ["O", "O", "O"],
        ["1", "1", "O"],
        ["1", "1", "O"],
        ["O", "O", "1"],
        ["O", "O", "1"],
        ["1", "1", "O"],
    ]
    expected = 3
    actual = num_islands(grid)
    assert actual == expected


def test_number_of_islands_5():
    grid = [
        ["1", "O", "O", "O", "O", "O"],
        ["1", "O", "1", "1", "1", "1"],
        ["O", "O", "O", "O", "O", "O"],
        ["1", "1", "1", "O", "1", "1"],
        ["1", "1", "1", "O", "1", "1"],
        ["O", "O", "O", "O", "1", "1"],
    ]
    expected = 4
    actual = num_islands(grid)
    assert actual == expected


def test_number_of_islands_6():
    grid = [
        ["1"],
    ]
    expected = 1
    actual = num_islands(grid)
    assert actual == expected


def test_number_of_islands_7():
    grid = [
        ["0"],
    ]
    expected = 0
    actual = num_islands(grid)
    assert actual == expected


def test_number_of_islands_8():
    grid = [["1", "1", "1"], ["0", "1", "0"], ["0", "1", "0"]]
    expected = 1
    actual = num_islands(grid)
    assert actual == expected
