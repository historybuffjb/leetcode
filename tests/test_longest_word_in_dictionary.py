from problems.longest_word_in_dictionary import longest_word


def test_longest_word_in_dictionary_1():
    words = ["w", "wo", "wor", "worl", "world"]
    expected = "world"
    actual = longest_word(words)
    assert actual == expected


def test_longest_word_in_dictionary_2():
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    expected = "apple"
    actual = longest_word(words)
    assert actual == expected


def test_longest_word_in_dictionary_3():
    words = ["a"]
    expected = "a"
    actual = longest_word(words)
    assert actual == expected


def test_longest_word_in_dictionary_4():
    words = ["bd", "b", "d"]
    expected = "bd"
    actual = longest_word(words)
    assert actual == expected


def test_longest_word_in_dictionary_5():
    words = ["a", "b", "ab"]
    expected = "ab"
    actual = longest_word(words)
    assert actual == expected


def test_longest_word_in_dictionary_6():
    words = ["bc", "b", "c", "a", "ab"]
    expected = "ab"
    actual = longest_word(words)
    assert actual == expected
