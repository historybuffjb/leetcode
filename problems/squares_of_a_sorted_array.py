"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number
sorted in non-decreasing order.
"""
from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    """
    Explanation
    The key here is that the array is sorted in non-decreasing order. Since we may may have negatives or positives,
    we can keep two pointers to read the positive and negative parts of the array. Since both pointers are then
    monotonic, we know that the final array will be monotonic.
    """
    if not nums:
        return nums
    result = [0] * len(nums)
    left = 0
    right = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = pow(square, 2)
    return result


"""
Run DETAILS
Runtime: 232 ms, faster than 53.11% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.1 MB, less than 61.71% of Python3 online submissions for Squares of a Sorted Array.
"""