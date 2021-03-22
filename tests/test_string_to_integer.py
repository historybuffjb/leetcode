from problems.string_to_integer import my_atoi


def test_string_to_integer_1():
    s = "42"
    expected = 42
    actual = my_atoi(s)
    assert actual == expected


def test_string_to_integer_2():
    s = "    -42"
    expected = -42
    actual = my_atoi(s)
    assert actual == expected


def test_string_to_integer_3():
    s = "4193 with words"
    expected = 4193
    actual = my_atoi(s)
    assert actual == expected


def test_string_to_integer_4():
    s = "words and 987"
    expected = 0
    actual = my_atoi(s)
    assert actual == expected


def test_string_to_integer_5():
    s = "-91283472332"
    expected = -2147483648
    actual = my_atoi(s)
    assert actual == expected


def test_string_to_integer_6():
    s = "+-12"
    expected = 0
    actual = my_atoi(s)
    assert actual == expected


def test_string_to_integer_7():
    s = "21474836460"
    expected = 2147483647
    actual = my_atoi(s)
    assert actual == expected


def test_string_to_integer_8():
    s = " "
    expected = 0
    actual = my_atoi(s)
    assert actual == expected


def test_string_to_integer_9():
    s = "2147483648"
    expected = 2147483647
    actual = my_atoi(s)
    assert actual == expected
