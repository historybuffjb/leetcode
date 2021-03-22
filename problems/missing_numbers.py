"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range
that is missing from the array.
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""
from typing import List


def missing_number(nums: List[int]) -> int:
    expected_sum = int(len(nums) * (len(nums) + 1) / 2)
    actual_sum = 0
    for val in nums:
        actual_sum += val
    return expected_sum - actual_sum


"""
Run DETAILS
Runtime: 188 ms, faster than 21.63% of Python3 online submissions for Missing Number.
Memory Usage: 15.4 MB, less than 82.71% of Python3 online submissions for Missing Number.
"""
