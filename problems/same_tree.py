"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
from test_utils import TreeNode


def _check_nodes(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return True


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """
    Explanation
    This problem involves two separate components:
        1. Checking that structurally they are the same.
        2. All values the same.
    To do this I believe we can traverse the tree and check at each node traversal value if both p and q node is the
    same.
    If at any time they are not the same node values we know that either the structure is different or the values
    of the same structure are different.
    """
    queue = [(p, q)]
    while queue:
        p, q = queue.pop(0)
        if not _check_nodes(p, q):
            return False
        # We now know these are equal so WLOG choose p
        if p:
            queue.append((p.left, q.left))
            queue.append((p.right, q.right))
    return True


"""
Run DETAILS
Runtime: 32 ms, faster than 61.93% of Python3 online submissions for Same Tree.
Memory Usage: 14.1 MB, less than 88.12% of Python3 online submissions for Same Tree.
"""
