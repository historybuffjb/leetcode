from problems.word_search_2 import find_words
from test_utils import compare_lists


def test_word_search_2_1():
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    expected = ["eat", "oath"]
    actual = find_words(board, words)
    assert compare_lists(expected, actual) is True


def test_word_search_2_2():
    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    expected = []
    actual = find_words(board, words)
    assert compare_lists(expected, actual) is True


def test_word_search_2_3():
    board = [
        ["j", "s", "o", "l", "u", "t", "i", "s"],
        ["s", "u", "n", "a", "r", "u", "u", "a"],
        ["n", "e", "p", "t", "u", "n", "e", "t"],
        ["s", "o", "n", "i", "e", "i", "s", "u"],
        ["r", "c", "e", "v", "t", "r", "e", "r"],
        ["a", "h", "t", "r", "a", "e", "s", "n"],
        ["m", "m", "e", "r", "c", "u", "r", "y"],
    ]
    words = [
        "earth",
        "jupiter",
        "mars",
        "mercury",
        "neptune",
        "saturn",
        "uranus",
        "venus",
    ]
    expected = ["earth", "mars", "mercury", "neptune", "saturn", "uranus"]
    actual = find_words(board, words)
    assert compare_lists(expected, actual) is True


def test_word_search_2_4():
    board = [["a"]]
    words = [
        "earth",
        "jupiter",
        "mars",
        "mercury",
        "neptune",
        "saturn",
        "uranus",
        "venus",
        "a",
    ]
    expected = ["a"]
    actual = find_words(board, words)
    assert compare_lists(expected, actual) is True
