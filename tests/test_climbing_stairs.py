from problems.climbing_stairs import climb_stairs


def test_climbing_stairs_1():
    n = 2
    expected = 2
    actual = climb_stairs(n)
    assert actual == expected


def test_climbing_stairs_2():
    n = 3
    expected = 3
    actual = climb_stairs(n)
    assert actual == expected


def test_climbing_stairs_3():
    n = 6
    expected = 13
    actual = climb_stairs(n)
    assert actual == expected


def test_climbing_stairs_4():
    n = 45
    expected = 1836311903
    actual = climb_stairs(n)
    assert actual == expected
