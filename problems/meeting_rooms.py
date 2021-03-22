"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person
could attend all meetings.
"""
from typing import List


def can_attend_meetings(intervals: List[List[int]]) -> bool:
    """
    Explanation
    With any overlapping interval problem we can certainly just brute force it in O(n^2) time. But here
    we can actually sort the intervals O(nlogn) quick sort in python and then ensure that the start of any interval
    is after the end of the previous end
    """
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


"""
Run DETAILS
Runtime: 76 ms, faster than 64.41% of Python3 online submissions for Meeting Rooms.
Memory Usage: 17.5 MB, less than 56.62% of Python3 online submissions for Meeting Rooms.
"""
