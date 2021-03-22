from problems.reverse_integer import reverse


def test_reverse_integer_1():
    x = 123
    expected = 321
    actual = reverse(x)
    assert actual == expected


def test_reverse_integer_2():
    x = -123
    expected = -321
    actual = reverse(x)
    assert actual == expected


def test_reverse_integer_3():
    x = 120
    expected = 21
    actual = reverse(x)
    assert actual == expected


def test_reverse_integer_4():
    x = 0
    expected = 0
    actual = reverse(x)
    assert actual == expected


def test_reverse_integer_5():
    x = 365
    expected = 563
    actual = reverse(x)
    assert actual == expected


def test_reverse_integer_6():
    x = -2147483648
    expected = 0
    actual = reverse(x)
    assert actual == expected
