"""
Given a text string and words (a list of strings), return all index pairs [i, j] so that the substring
text[i]...text[j] is in the list of words.
"""
from collections import defaultdict
from functools import reduce
from typing import List


def index_pairs(text: str, words: List[str]) -> List[List[int]]:
    """
    Explanation
    We have a list of words. We can generate a Trie tree from the letters of these words and then do a single
    passthrough of text. At each letter of text we traverse the tree until we find the end of the word. This ending
    is another index to append. If we ever reach the end of text in this traversal we can move to the next letter.
    """
    trie = {}
    res = []
    end_sign = "$"
    for word in words:
        temp = trie
        for letter in word:
            if letter not in temp.keys():
                temp[letter] = {}
            temp = temp[letter]
        temp[end_sign] = True
    for start in range(len(text)):
        temp = trie
        letter = text[start]
        end = start
        while letter in temp.keys():
            temp = temp[letter]
            if end_sign in temp.keys():
                res.append([start, end])
            end += 1
            if end == len(text):
                break
            letter = text[end]
    return res


"""
Run DETAILS
Runtime: 40 ms, faster than 73.81% of Python3 online submissions for Index Pairs of a String.
Memory Usage: 14.4 MB, less than 75.51% of Python3 online submissions for Index Pairs of a String.
"""
