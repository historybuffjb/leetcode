"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n
vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two
lines, which, together with the x-axis forms a container, such that the container contains the most water.
Notice that you may not slant the container.
"""
from typing import List


def max_area(height: List[int]) -> int:
    """
    Explanation
    The key thing here is that we need to find two lines separately, which together form a container with the most
    water. We can do this by using a left and right pointer, and start at the end. We will progressively move
    right for the left counter and left for the right counter. At each change we make the following choices:
        * Pick the largest line. Move the other towards the middle.
        * If we ever cross the left and right pointers we can stop and return the found maximum.
    """
    left = 0
    right = len(height) - 1
    largest = 0
    while left < right:
        largest = max(largest, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return largest


"""
Runtime: 716 ms, faster than 19.84% of Python3 online submissions for Container With Most Water.
Memory Usage: 26.5 MB, less than 21.55% of Python3 online submissions for Container With Most Water.
"""
