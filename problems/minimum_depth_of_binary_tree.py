"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
"""
from test_utils import TreeNode


def min_depth(root: TreeNode) -> int:
    """
    Explanation
    The key here is depth. To get the depth of a tree we can use breadth-first search to keep track of the level
    we are at. The minimum number of nodes to reach a leaf will be defined as the level of the leaf.
    """
    if not root:
        return 0
    queue = [(root, 1)]
    while queue:
        node, level = queue.pop(0)
        if node.left is None and node.right is None:
            # Reached a leaf
            return level
        if node.left is not None:
            queue.append((node.left, level + 1))
        if node.right is not None:
            queue.append((node.right, level + 1))


"""
Run DETAILS
Runtime: 492 ms, faster than 72.53% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 49.1 MB, less than 87.97% of Python3 online submissions for Minimum Depth of Binary Tree.
"""
