"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""
from test_utils import TreeNode


def diameter_of_binary_tree(root: TreeNode) -> int:
    """
    Explanation
    The diameter of a binary tree does not have to go to the root. But, we do know that the longest path must
    be from two leaf nodes. If not we could extend another edge and it would not be the diameter. Thus we know that
    the longest length will include some node and its longest left path and longest right path (maybe root) and
    so we just keep track of the sum of its longest left and right branches and check the maximum depth.
    """
    diameter = 0

    def longest_path_util(node: TreeNode) -> int:
        if node is None:
            return 0
        nonlocal diameter
        left = longest_path_util(node.left)
        right = longest_path_util(node.right)
        diameter = max(diameter, left + right)
        return max(left, right) + 1

    longest_path_util(root)
    return diameter


"""
Run DETAILS
Runtime: 44 ms, faster than 72.52% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 16.4 MB, less than 22.99% of Python3 online submissions for Diameter of Binary Tree.
"""
