"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """
    Explanation
    We need a quick way to reference elements. We can define a subproblem as a given index i to be the following:
        * Calculate the product of elements left of i
        * Calculate the product of elements right of i
        * Multiple them together
    So we can think of this from a DP perspective. We keep two arrays:
        * left - at index i holds the product of i - 1 -> 0 elements
        * right - at index i holds the product of n - 1 -> i + 1 elements
    We then iterate through nums creating a final arr
    """
    left = [0] * len(nums)
    right = [0] * len(nums)
    result = [0] * len(nums)
    # Populate left
    left[0] = 1
    for i in range(1, len(left)):
        left[i] = nums[i - 1] * left[i - 1]
    # Populate right
    right[len(nums) - 1] = 1
    for i in range(len(nums) - 2, -1, -1):
        right[i] = nums[i + 1] * right[i + 1]
    for i in range(len(nums)):
        result[i] = left[i] * right[i]
    return result


"""
Run DETAILS
Runtime: 244 ms, faster than 61.68% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 22.3 MB, less than 27.95% of Python3 online submissions for Product of Array Except Self.
"""
