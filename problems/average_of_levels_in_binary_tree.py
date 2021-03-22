"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
Answers within 10^-5 of the actual answer will be accepted.
"""
from typing import List
from test_utils import TreeNode


def average_of_levels(root: TreeNode) -> List[float]:
    """
    Explanation
    Since we care about levels of a binary tree, the important thing to realize is that BFS will shine here.
    We will keep track of which level we are on, accumulating the sum of the current level and the count of
    nodes at each level. If we have encountered a node with a level greater than our current level,
    we will calculate the average of the previous level and add that to the result.
    """
    queue = [(root, 0)]
    result_arr = []
    cur_level = cur_count = cur_sum = 0
    while queue:
        node, level = queue.pop(0)
        if level > cur_level:
            result_arr.append(float(cur_sum / cur_count))
            cur_level += 1
            cur_sum = cur_count = 0
        cur_sum += node.val
        cur_count += 1
        if node.left is not None:
            queue.append((node.left, level + 1))
        if node.right is not None:
            queue.append((node.right, level + 1))
    result_arr.append(float(cur_sum / cur_count))
    return result_arr


"""
Run DETAILS
Runtime: 52 ms, faster than 55.44% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 16.6 MB, less than 36.25% of Python3 online submissions for Average of Levels in Binary Tree.
"""