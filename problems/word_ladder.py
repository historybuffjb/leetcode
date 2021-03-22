"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of
words such that:
    * The first word in the sequence is beginWord.
    * The last word in the sequence is endWord.
    * Only one letter is different between each adjacent pair of words in the sequence.
    * Every word in the sequence is in wordList.
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
"""
from collections import defaultdict, deque
from typing import List


def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    pass


"""
Run DETAILS
Runtime: 140 ms, faster than 67.41% of Python3 online submissions for Word Ladder.
Memory Usage: 18.3 MB, less than 17.89% of Python3 online submissions for Word Ladder.
"""