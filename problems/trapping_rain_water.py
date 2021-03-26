"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""
from typing import List


def trap(height: List[int]) -> int:
    """
    Explanation
    The basic idea here is a simple left right array problem. We start at the far left and far right and make the
    following decision at each iteration while keeping track of the largest left and right seen:
        * if current height left < current height right:
            * Check if we have a new largest left:
                * If so update largest left else we can accumulate largest left - current left amount of water
            * increment left
        * If current height left >= current height right:
            * Check if we have a new largest right:
                * If so update largest right else we can accumulate largest right - current right amount of water
            * decrement right
    """
    left = 0
    right = len(height) - 1
    largest_left = 0
    largest_right = 0
    result = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= largest_left:
                largest_left = height[left]
            else:
                result += largest_left - height[left]
            left += 1
        else:
            if height[right] >= largest_right:
                largest_right = height[right]
            else:
                result += largest_right - height[right]
            right -= 1
    return result


"""
Run DETAILS
Runtime: 52 ms, faster than 80.91% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 14.6 MB, less than 99.82% of Python3 online submissions for Trapping Rain Water.
"""
