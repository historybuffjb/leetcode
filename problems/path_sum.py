"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such
that adding up all the values along the path equals targetSum.
A leaf is a node with no children.
"""
from test_utils import TreeNode


def has_path_sum(root: TreeNode, target_sum: int) -> bool:
    """
    Explanation
    Here we want to try to find target_sum in the graph from root to leaf. Thus we probably want to try DFS
    because it goes deep instead of wide. The idea is as follows:
    1. We will use a stack to do a DFS of the graph. At each new node we will keep track of it's sum + its parents sum
    2. If we have reached a leaf node we check if current sum == target_sum. If so return False
    3. If we never found target_sum we return False
    """
    if root is None:
        return False
    queue = [(root, root.val)]
    while queue:
        node, cur_sum = queue.pop(-1)
        if node.left is None and node.right is None and cur_sum == target_sum:
            return True
        if node.left:
            queue.append((node.left, cur_sum + node.left.val))
        if node.right:
            queue.append((node.right, cur_sum + node.right.val))
    return False


"""
Run DETAILS
Runtime: 36 ms, faster than 95.29% of Python3 online submissions for Path Sum.
Memory Usage: 16 MB, less than 50.72% of Python3 online submissions for Path Sum.
"""

