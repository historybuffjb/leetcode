"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the
farthest leaf node.
"""
from test_utils import TreeNode


def max_depth(root: TreeNode) -> int:
    """
    Explanation
    To find a tree's maximum depth we will have to traverse the tree. Since we care about depth instead of breadth
    we should use DFS. The key will be to track the height (level) of the tree and a maximum level found.
    """
    if root is None:
        return 0
    stack = [(root, 1)]
    result = 0
    while stack:
        node, level = stack.pop(-1)
        if level > result:
            result = level
        if node.left is not None:
            stack.append((node.left, level + 1))
        if node.right is not None:
            stack.append((node.right, level + 1))
    return result


"""
Run DETAILS
Runtime: 40 ms, faster than 76.55% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.2 MB, less than 97.45% of Python3 online submissions for Maximum Depth of Binary Tree.
"""