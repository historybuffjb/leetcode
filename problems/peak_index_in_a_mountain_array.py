"""
Let's call an array arr a mountain if the following properties hold:
    * arr.length >= 3
    * There exists some i with 0 < i < arr.length - 1 such that:
        * arr[0] < arr[1] < ... arr[i-1] < arr[i]
        * arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that
arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
"""
from typing import List


def peak_index_in_mountain_array(arr: List[int]) -> int:
    """
    Explanation
    The key here is to find the peak. We technically have two sorted arrays with a peak in the middle. Since we have
    two sorted arrays inside we can probably use binary search. To do this we can make the following rules
        * If our midpoint is sorted in ascending order, we need to move right and vise versa.
        * Since arr is guaranteed to have a peak we will find the answer using this algorithm (loop invariant)
    """
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


"""
Run DETAILS
Runtime: 68 ms, faster than 94.78% of Python3 online submissions for Peak Index in a Mountain Array.
Memory Usage: 15.3 MB, less than 57.96% of Python3 online submissions for Peak Index in a Mountain Array.
"""