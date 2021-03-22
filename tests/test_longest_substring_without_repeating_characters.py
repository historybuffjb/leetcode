from problems.longest_substring_without_repeating_characters import (
    length_of_longest_substring,
)


def test_longest_substring_without_repeating_characters_1():
    s: str = "abcabcbb"
    expected: int = 3
    actual = length_of_longest_substring(s)
    assert actual == expected


def test_longest_substring_without_repeating_characters_2():
    s: str = "bbbbb"
    expected: int = 1
    actual = length_of_longest_substring(s)
    assert actual == expected


def test_longest_substring_without_repeating_characters_3():
    s: str = "pwwkew"
    expected: int = 3
    actual = length_of_longest_substring(s)
    assert actual == expected


def test_longest_substring_without_repeating_characters_4():
    s: str = ""
    expected: int = 0
    actual = length_of_longest_substring(s)
    assert actual == expected


def test_longest_substring_without_repeating_characters_5():
    s: str = " "
    expected: int = 1
    actual = length_of_longest_substring(s)
    assert actual == expected
