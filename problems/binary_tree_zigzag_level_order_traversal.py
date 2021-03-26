"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).
"""
from collections import deque
from typing import List

from test_utils import TreeNode


def zig_zag_level_order(root: TreeNode) -> List[List[int]]:
    """
    Explanation
    This is a simple BFS. The only difference is we need to know 2 things:
        * When a level ends to append a new array to our result
        * Whether we are moving right or left so we know in which order to insert into our temp list
    """
    if root is None:
        return []
    result = []
    cur_list = deque()
    # start with the level 0 with a delimiter
    queue = [root, None]
    direction_left = True
    while queue:
        curr_node = queue.pop(0)
        if curr_node:
            if direction_left:
                cur_list.append(curr_node.val)
            else:
                cur_list.appendleft(curr_node.val)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        else:
            result.append(list(cur_list))
            if queue:
                queue.append(None)
            cur_list = deque()
            direction_left = not direction_left
    return result


"""
Runtime: 32 ms, faster than 69.05% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 14.5 MB, less than 74.65% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
"""
