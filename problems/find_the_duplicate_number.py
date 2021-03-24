"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
"""
from typing import List


def find_duplicate(nums: List[int]) -> int:
    """
    Explanation
    We are given the fact that there is exactly one duplicate in our array. If we think of this list as a linked list,
    we are guaranteed a single cycle. Thus this is a perfect candidate for floyd's algorithm. The basic idea goes like
    this:
        * We have a tortoise and a hare. The hare moves twice as start as a tortoise to start.
        * Eventually we will reach a point where hare and tortoise are at the same spot (the cycle)
        * We then reset the tortoise to root and traverse both tortoise and the hare one increment at a time
        and whenever they end up at the same point we have reached our cycle point.
    """
    tortoise = hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    return hare


"""
Run DETAILS
Runtime: 68 ms, faster than 54.88% of Python3 online submissions for Find the Duplicate Number.
Memory Usage: 16.5 MB, less than 77.89% of Python3 online submissions for Find the Duplicate Number.
"""