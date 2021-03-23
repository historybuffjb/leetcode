from problems.index_pairs_of_a_string import index_pairs
from test_utils import compare_lists

DEBUG = False


def test_index_pairs_of_a_string_1():
    text = "thestoryofleetcodeandme"
    words = ["story", "fleet", "leetcode"]
    expected = [[3, 7], [9, 13], [10, 17]]
    actual = index_pairs(text, words)
    assert compare_lists(expected, actual, DEBUG) is True


def test_index_pairs_of_a_string_2():
    text = "ababa"
    words = ["aba", "ab"]
    expected = [[0, 1], [0, 2], [2, 3], [2, 4]]
    actual = index_pairs(text, words)
    assert compare_lists(expected, actual, DEBUG) is True


def test_index_pairs_of_a_string_3():
    text = "a"
    words = ["aba", "ab", "adbc"]
    expected = []
    actual = index_pairs(text, words)
    assert compare_lists(expected, actual, DEBUG) is True


def test_index_pairs_of_a_string_4():
    text = "thisisleetcode"
    words = ["a"]
    expected = []
    actual = index_pairs(text, words)
    assert compare_lists(expected, actual, DEBUG) is True
