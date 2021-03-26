from problems.word_break import word_break


def test_word_break_1():
    s = "leetcode"
    word_dict = ["leet", "code"]
    expected = True
    actual = word_break(s, word_dict)
    assert actual == expected


def test_word_break_2():
    s = "applepenapple"
    word_dict = ["apple", "pen"]
    expected = True
    actual = word_break(s, word_dict)
    assert actual == expected


def test_word_break_3():
    s = "catsandog"
    word_dict = ["cats", "dog", "sand", "and", "cat"]
    expected = False
    actual = word_break(s, word_dict)
    assert actual == expected


def test_word_break_4():
    s = "a"
    word_dict = ["test"]
    expected = False
    actual = word_break(s, word_dict)
    assert actual == expected


def test_word_break_5():
    s = "a"
    word_dict = ["test"]
    expected = False
    actual = word_break(s, word_dict)
    assert actual == expected


def test_word_break_6():
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
    expected = False
    actual = word_break(s, word_dict)
    assert actual == expected
