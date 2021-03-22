from problems.backspace_string_compare import backspace_compare


def test_backspace_string_compare_1():
    s = "ab#c"
    t = "ad#c"
    expected = True
    actual = backspace_compare(s, t)
    assert actual == expected


def test_backspace_string_compare_2():
    s = "ab##"
    t = "c#d#"
    expected = True
    actual = backspace_compare(s, t)
    assert actual == expected


def test_backspace_string_compare_3():
    s = "a##c"
    t = "#a#c"
    expected = True
    actual = backspace_compare(s, t)
    assert actual == expected


def test_backspace_string_compare_4():
    s = "a#c"
    t = "b"
    expected = False
    actual = backspace_compare(s, t)
    assert actual == expected


def test_backspace_string_compare_5():
    s = "##########"
    t = "#"
    expected = True
    actual = backspace_compare(s, t)
    assert actual == expected


def test_backspace_string_compare_6():
    s = "a"
    t = "c"
    expected = False
    actual = backspace_compare(s, t)
    assert actual == expected
