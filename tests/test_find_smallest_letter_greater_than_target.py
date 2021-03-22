from problems.find_smallest_letter_greater_than_target import next_greatest_letter


def test_find_smallest_letter_greater_than_target_1():
    letters = ["c", "f", "j"]
    target = "a"
    expected = "c"
    actual = next_greatest_letter(letters, target)
    assert actual == expected


def test_find_smallest_letter_greater_than_target_2():
    letters = ["c", "f", "j"]
    target = "c"
    expected = "f"
    actual = next_greatest_letter(letters, target)
    assert actual == expected


def test_find_smallest_letter_greater_than_target_3():
    letters = ["c", "f", "j"]
    target = "d"
    expected = "f"
    actual = next_greatest_letter(letters, target)
    assert actual == expected


def test_find_smallest_letter_greater_than_target_4():
    letters = ["c", "f", "j"]
    target = "g"
    expected = "j"
    actual = next_greatest_letter(letters, target)
    assert actual == expected


def test_find_smallest_letter_greater_than_target_5():
    letters = ["c", "f", "j"]
    target = "j"
    expected = "c"
    actual = next_greatest_letter(letters, target)
    assert actual == expected


def test_find_smallest_letter_greater_than_target_6():
    letters = ["c", "f", "j"]
    target = "k"
    expected = "c"
    actual = next_greatest_letter(letters, target)
    assert actual == expected


def test_find_smallest_letter_greater_than_target_7():
    letters = ["x", "y"]
    target = "a"
    expected = "x"
    actual = next_greatest_letter(letters, target)
    assert actual == expected


def test_find_smallest_letter_greater_than_target_8():
    letters = ["x", "y"]
    target = "z"
    expected = "x"
    actual = next_greatest_letter(letters, target)
    assert actual == expected
