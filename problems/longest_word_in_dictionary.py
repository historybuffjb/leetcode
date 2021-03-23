"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built
one character at a time by other words in words. If there is more than one possible answer, return the longest
word with the smallest lexicographical order.
If there is no answer, return the empty string.
"""
import collections
from functools import reduce
from typing import List


def longest_word(words: List[str]) -> str:
    """
    Explanation
    Put every word in a trie, then depth-first-search from the start of the trie, only searching nodes that ended a
    word. Every node found (except the root, which is a special case) then represents a word with all it's prefixes
    present. We take the best such word.
    """
    trie_type = lambda: collections.defaultdict(trie_type)
    trie = trie_type()
    end_sign = True
    for i, word in enumerate(words):
        reduce(dict.__getitem__, word, trie)[end_sign] = i
    stack = list(trie.values())
    ans = ""
    while stack:
        cur = stack.pop()
        if end_sign in cur:
            word = words[cur[end_sign]]
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                ans = word
            stack.extend([cur[letter] for letter in cur if letter != end_sign])
    return ans


"""
Run DETAILS
Runtime: 112 ms, faster than 59.67% of Python3 online submissions for Longest Word in Dictionary.
Memory Usage: 15.2 MB, less than 31.06% of Python3 online submissions for Longest Word in Dictionary.
"""
