from problems.word_break_2 import word_break
from test_utils import compare_lists


def test_word_break_2_1():
    s = "catsanddog"
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    expected = ["cats and dog", "cat sand dog"]
    actual = word_break(s, word_dict)
    assert compare_lists(expected, actual) is True


def test_word_break_2_2():
    s = "pineapplepenapple"
    word_dict = ["apple", "pen", "applepen", "pine", "pineapple"]
    expected = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
    actual = word_break(s, word_dict)
    assert compare_lists(expected, actual) is True


def test_word_break_2_3():
    s = "catsandog"
    word_dict = ["cats", "dog", "sand", "and", "cat"]
    expected = []
    actual = word_break(s, word_dict)
    assert compare_lists(expected, actual) is True


def test_word_break_2_4():
    s = "catsanddogo"
    word_dict = ["cat", "cats", "and", "sand", "dog", "do", "go"]
    expected = ["cat sand do go", "cats and do go"]
    actual = word_break(s, word_dict)
    assert compare_lists(expected, actual) is True


def test_word_break_2_5():
    s = "b"
    word_dict = ["aabbb"]
    expected = []
    actual = word_break(s, word_dict)
    assert compare_lists(expected, actual) is True


def test_word_break_2_6():
    s = "pineapplepenapple"
    word_dict = []
    expected = []
    actual = word_break(s, word_dict)
    assert compare_lists(expected, actual) is True


def test_word_break_2_7():
    s = ""
    word_dict = []
    expected = []
    actual = word_break(s, word_dict)
    assert compare_lists(expected, actual) is True


def test_word_break_2_8():
    s = ""
    word_dict = ["cat", "cats", "and", "sand", "dog", "do", "go"]
    expected = []
    actual = word_break(s, word_dict)
    assert compare_lists(expected, actual) is True


def test_word_break_2_9():
    s = "ifindleetcodefun"
    word_dict = [
        "i",
        "leet",
        "leetcode",
        "code",
        "fun",
        "find",
        "codefun",
        "test",
        "do",
    ]
    expected = ["i find leetcode fun", "i find leet code fun", "i find leet codefun"]
    actual = word_break(s, word_dict)
    assert compare_lists(expected, actual) is True


def test_word_break_2_10():
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa "
    word_dict = [
        "a",
        "aa",
        "aaa",
        "aaaa",
        "aaaaa",
        "aaaaaa",
        "aaaaaaa",
        "aaaaaaaa",
        "aaaaaaaaa",
        "aaaaaaaaaa",
    ]
    expected = []
    actual = word_break(s, word_dict)
    assert compare_lists(expected, actual) is True
