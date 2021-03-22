"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
"""
from typing import List


def single_number(nums: List[int]) -> int:
    """
    Explanation
    XOR exhibits the following properties:
        * a xor 0 = a
        * a xor a = 0
        * a xor b xor a = (a xor a) xor b = 0 xor b = b
    Thus we just need to xor starting at 0 and return the result (since it is a unique number)
    """
    result = 0
    for num in nums:
        result ^= num
    return result


"""
Run DETAILS
Runtime: 148 ms, faster than 34.01% of Python3 online submissions for Single Number.
Memory Usage: 16.5 MB, less than 86.39% of Python3 online submissions for Single Number.
"""
