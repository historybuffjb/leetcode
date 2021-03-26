"""
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    result = []
    for interval in intervals:
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result


"""
Run DETAILS
Runtime: 76 ms, faster than 97.43% of Python3 online submissions for Merge Intervals.
Memory Usage: 16.2 MB, less than 56.17% of Python3 online submissions for Merge Intervals.
"""
