"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search
target in nums. If target exists, then return its index. Otherwise, return -1.
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


"""
Run DETAILS
Runtime: 232 ms, faster than 83.25% of Python3 online submissions for Binary Search.
Memory Usage: 15.6 MB, less than 70.14% of Python3 online submissions for Binary Search.
"""
