"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as
the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
from test_utils import TreeNode


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Explanation
    The key here is that this is a BST. The basic idea is we can traverse the tree until we get to the point
    where p and q have values that don't lead to traversing the same child. At that point you know you have the
    LCA.
    """
    node = root
    while node is not None:
        if p.val > node.val and q.val > node.val:
            node = node.right
        elif p.val < node.val and q.val < node.val:
            node = node.left
        else:
            return node
    return None


"""
Run DETAILS
Runtime: 68 ms, faster than 97.33% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 18.3 MB, less than 70.69% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
"""