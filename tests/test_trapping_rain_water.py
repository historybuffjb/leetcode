from problems.trapping_rain_water import trap


def test_trapping_rain_water_1():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    expected = 6
    actual = trap(height)
    assert actual == expected


def test_trapping_rain_water_2():
    height = [4, 2, 0, 3, 2, 5]
    expected = 9
    actual = trap(height)
    assert actual == expected
