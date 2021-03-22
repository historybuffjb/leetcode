"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a
subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could
also be considered as a subtree of itself.
"""
from test_utils import TreeNode


def _identical(a: TreeNode, b: TreeNode) -> bool:
    if not a and not b:
        return True
    if not a or not b:
        return False
    return a.val == b.val and _identical(a.left, b.left) and _identical(a.right, b.right)


def is_subtree(s: TreeNode, t: TreeNode) -> bool:
    """
    Explanation
    The key thing here is that we can look traverse the tree and check the substructure at any point. Thus
    what we can do is check if s and t are identical, and if not recursively do the same thing. If no substructure
    is ever found return False else return True
    """
    if t is None:
        return True
    if s is None:
        return False
    if _identical(s, t):
        return True
    return is_subtree(s.left, t) or is_subtree(s.right, t)


"""
Run DETAILS
Runtime: 252 ms, faster than 44.38% of Python3 online submissions for Subtree of Another Tree.
Memory Usage: 15.7 MB, less than 5.88% of Python3 online submissions for Subtree of Another Tree.
"""