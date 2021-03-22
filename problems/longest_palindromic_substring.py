"""
Given a string s, return the longest palindromic substring in s.
"""


def get_max_len(s: str, left: int, right: int) -> int:
    length = len(s)
    i = 1
    max_len = 0
    while left >= 0 and right < length and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


def longest_palindrome(s: str) -> str:
    """
    Explanation:
        * I first tried a dp solution. For some reason this timed out so here is an alternative solution that
            * I did not come up with myself
        * We first recognize that any palindrome expands from its center and can be compared from its center
        * We have two choices, odd or even. If even, we would want to expand from its center 2, ex. abba
            * If odd, we just expand from the exact center, ex. aba
        * If we get the max length of these two expansions and compare it to the current start and end values,
            * we can update our start and end values based on the following
                * Start = current index - the floor of cur_max  - 1 / 2
                * End = current index + the floor of cur_max / 2
    """
    if len(s) <= 1:
        return s
    start = end = 0
    length = len(s)
    for i in range(length):
        max_len_1 = get_max_len(s, i, i + 1)
        max_len_2 = get_max_len(s, i, i)
        max_len = max(max_len_1, max_len_2)
        if max_len > end - start + 1:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    return s[start : end + 1]


"""
Run DETAILS
Runtime: 856 ms, faster than 85.67% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.4 MB, less than 39.86% of Python3 online submissions for Longest Palindromic Substring.
"""
