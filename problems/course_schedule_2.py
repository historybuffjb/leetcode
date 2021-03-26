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
    """
    Explanation
    This is a classic topological sort. We build a graph represented as an adjacency list and do a depth first
    search using Kahn's algorithm for topological sorting. If at the end we have more elements in our topologically
     sorted list than there is a cycle, and we return an empty list.
    """
    if not num_courses:
        return []
    result = []
    graph = defaultdict(list)
    node_degrees = {}
    # Build graph
    for prq, cls in prerequisites:
        graph[cls].append(prq)
        node_degrees[prq] = node_degrees.get(prq, 0) + 1
    # Make queue
    queue = []
    # Enqueue 0 degree nodes
    for i in range(num_courses):
        if i not in node_degrees:
            queue.append(i)
    while queue:
        node = queue.pop(0)
        result.append(node)
        if node in graph:
            for adj in graph[node]:
                node_degrees[adj] -= 1
                if node_degrees[adj] == 0:
                    queue.append(adj)
    return result if len(result) == num_courses else []


"""
Run DETAILS
Runtime: 92 ms, faster than 94.66% of Python3 online submissions for Course Schedule II.
Memory Usage: 15.5 MB, less than 89.98% of Python3 online submissions for Course Schedule II.
"""
