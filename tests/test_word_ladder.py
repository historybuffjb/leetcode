from problems.word_ladder import ladder_length


def test_word_ladder_1():
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected = 5
    actual = ladder_length(begin_word, end_word, word_list)
    assert actual == expected


def test_word_ladder_2():
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log"]
    expected = 0
    actual = ladder_length(begin_word, end_word, word_list)
    assert actual == expected


def test_word_ladder_3():
    begin_word = "toon"
    end_word = "plea"
    word_list = ["poon", "plee", "same", "poie", "plea", "plie", "poin"]
    expected = 7
    actual = ladder_length(begin_word, end_word, word_list)
    assert actual == expected


def test_word_ladder_4():
    begin_word = "abcv"
    end_word = "ebad"
    word_list = ["abcd", "ebad", "ebcd", "xyza"]
    expected = 4
    actual = ladder_length(begin_word, end_word, word_list)
    assert actual == expected
