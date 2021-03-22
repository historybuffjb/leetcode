"""
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find
the smallest element in the list that is larger than the given target.
Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
"""
from typing import List


def next_greatest_letter(letters: List[str], target: str) -> str:
    """
    Explanation
    Since we have a sorted list we can assume binary search. The idea here is to traverse using binary search and
    at the end return left % len(letters)
    """
    left = 0
    right = len(letters)
    while left < right:
        mid = left + (right - left) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return letters[left % len(letters)]


"""
Run DETAILS
Runtime: 100 ms, faster than 96.65% of Python3 online submissions for Find Smallest Letter Greater Than Target.
Memory Usage: 14.3 MB, less than 95.32% of Python3 online submissions for Find Smallest Letter Greater Than Target.
"""