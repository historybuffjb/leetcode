"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each
word is a valid dictionary word. Return all such possible sentences in any order.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""
from collections import defaultdict
from typing import List, Union


def _work_break_dfs(s: str, word_dict: List[str]) -> List[str]:
    pass


def word_break(s: str, word_dict: List[str]) -> List[str]:
    """
    Explanation
    The basic idea is to use recursion. We can recursively do the following with memoization
        * Loop through the current input string and check if we have found a word.
            * If so, recursively check for other words and get a list of all possible solutions for current word
        * At the end return our total accumulated sub problems.
        * We can optimize a little bit by checking for subproblems before recursion to avoid extra work.
    """
    word_set = set(word_dict)
    memo = defaultdict(list)

    def _word_break_recurse(temp_str: str):
        nonlocal word_set
        nonlocal memo
        if not temp_str:
            return [[]]
        if temp_str in memo:
            return memo[temp_str]
        for endIndex in range(1, len(temp_str) + 1):
            word = temp_str[:endIndex]
            if word in word_set:
                for sub_problems in _word_break_recurse(temp_str[endIndex:]):
                    memo[temp_str].append([word] + sub_problems)
        return memo[temp_str]

    _word_break_recurse(s)
    return [" ".join(words) for words in memo[s]]


"""
Run DETAILS
Runtime: 24 ms, faster than 98.04% of Python3 online submissions for Word Break II.
Memory Usage: 14.1 MB, less than 96.01% of Python3 online submissions for Word Break II.
"""
