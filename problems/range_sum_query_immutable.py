"""
Given an integer array nums, find the sum of the elements between indices left and right inclusive, where
(left <= right).
Implement the NumArray class:
    * NumArray(int[] nums) initializes the object with the integer array nums.
    * int sumRange(int left, int right) returns the sum of the elements of the nums array in the range [left, right]
        inclusive (i.e., sum(nums[left], nums[left + 1], ... , nums[right])).
"""
from typing import List


class NumArray:
    """
    Explanation
    First we notice that we certainly can just store nums and then each time sum_range is called we can sum what we
    need. But this is very slow even if time complexity is O(1).
    Thus what we can first preprocess in 0(len(nums)) time by having sum[i] be the sum of the 0....i-1 previous elements
    So sum_range ends up being sum[right + 1] - sum[left]
    """

    def __init__(self, nums: List[int]):
        self.sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.sum[i + 1] = self.sum[i] + nums[i]

    def sum_range(self, left: int, right: int) -> int:
        return self.sum[right + 1] - self.sum[left]


"""
Run DETAILS
Runtime: 80 ms, faster than 71.39% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 17.8 MB, less than 47.70% of Python3 online submissions for Range Sum Query - Immutable.
"""
