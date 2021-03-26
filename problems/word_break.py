"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""
from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    """
    Explanation
    """
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]


"""
Run DETAILS
Runtime: 32 ms, faster than 93.10% of Python3 online submissions for Word Break.
Memory Usage: 14.5 MB, less than 47.41% of Python3 online submissions for Word Break.
"""
