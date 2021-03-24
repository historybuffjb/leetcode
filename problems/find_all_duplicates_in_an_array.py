"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?
"""
from typing import List


def find_duplicates(nums: List[int]) -> List[int]:
    """
    Explanation
    The key hint we are given here is that the integers are in the range 1:n where n is the length of the array.
    So that means every element in nums can map to an index of nums. So the basic algorithm here is this:
        * Loop through the array, setting the current num value's index in the array to a negative. * -1
        * If we ever encounter an element that is negative, we have seen this index before
    """
    result = []
    for num in nums:
        if nums[abs(num) - 1] < 0:
            result.append(abs(num))
        nums[abs(num) - 1] *= -1
    return result


"""
Run DETAILS
Runtime: 364 ms, faster than 64.23% of Python3 online submissions for Find All Duplicates in an Array.
Memory Usage: 21.7 MB, less than 76.94% of Python3 online submissions for Find All Duplicates in an Array.
"""