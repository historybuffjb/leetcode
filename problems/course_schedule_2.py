"""
There are a total of n courses you have to take labelled from 0 to n - 1.
Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you
must take the course bi before the course ai.
Given the total number of courses numCourses and a list of the prerequisite pairs, return the
ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""
from collections import defaultdict, deque
from typing import List


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    pass