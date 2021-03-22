"""
Given the root of a binary tree, invert the tree, and return its root.
"""
from test_utils import TreeNode


def invert_tree(root: TreeNode) -> TreeNode:
    """
    Explanation
    To invert a binary tree we need to reverse top down. Thus at root we swap the whole subtrees and iteratively do this
    all the way down the tree. This is really just a BFS with swapping each node's children.
    """
    if root is None:
        return None
    queue = [root]
    while queue:
        node = queue.pop(0)
        # Swap pointers
        temp = node.left
        node.left = node.right
        node.right = temp
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return root


"""
Run DETAILS
Runtime: 28 ms, faster than 86.23% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.4 MB, less than 12.11% of Python3 online submissions for Invert Binary Tree.
"""
