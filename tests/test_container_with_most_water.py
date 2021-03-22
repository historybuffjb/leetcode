from problems.container_with_most_water import max_area


def test_container_with_most_water_1():
    height = [1, 1]
    expected = 1
    actual = max_area(height)
    assert actual == expected


def test_container_with_most_water_2():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    expected = 49
    actual = max_area(height)
    assert actual == expected


def test_container_with_most_water_3():
    height = [4, 3, 2, 1, 4]
    expected = 16
    actual = max_area(height)
    assert actual == expected


def test_container_with_most_water_4():
    height = [1, 2, 1]
    expected = 2
    actual = max_area(height)
    assert actual == expected
