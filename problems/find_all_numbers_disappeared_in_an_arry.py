"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""
from typing import List


def find_disappeared_number(nums: List[int]) -> List[int]:
    result_hash = {}
    result = []
    for num in nums:
        result_hash[num] = None
    for i in range(1, len(nums) + 1):
        if i not in result_hash:
            result.append(i)
    return result


"""
Run DETAILS
Runtime: 332 ms, faster than 86.97% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 23.5 MB, less than 37.74% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""