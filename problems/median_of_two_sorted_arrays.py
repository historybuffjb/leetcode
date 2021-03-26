"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
"""
from typing import List


def find_median_sorted_array(nums_1: List[int], nums_2: List[int]) -> float:
    m, n = len(nums_1), len(nums_2)
    if m > n:
        nums_1, nums_2, m, n = nums_2, nums_1, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and nums_2[j - 1] > nums_1[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and nums_1[i - 1] > nums_2[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0:
                max_of_left = nums_2[j - 1]
            elif j == 0:
                max_of_left = nums_1[i - 1]
            else:
                max_of_left = max(nums_1[i - 1], nums_2[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = nums_2[j]
            elif j == n:
                min_of_right = nums_1[i]
            else:
                min_of_right = min(nums_1[i], nums_2[j])

            return (max_of_left + min_of_right) / 2.0


"""
Run DETAILS
Runtime: 92 ms, faster than 69.20% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.4 MB, less than 81.10% of Python3 online submissions for Median of Two Sorted Arrays.
"""
