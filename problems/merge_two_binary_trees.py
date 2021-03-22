"""
You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others
are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum
node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new
tree.
Return the merged tree.
Note: The merging process must start from the root nodes of both trees.
"""
from test_utils import TreeNode


def merge_trees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    """
    Explanation
    Since we are merging two binary trees we need to traverse the trees. We can do this with BFS or DFS and in this
    case I choose DFS. The idea is that we migrate root1 to be the final TreeNode.
        1. If we have a match between root1 and root2 we will sum them together and include them in the result
        2. If we don't have a match we just include either root1 or root2 in result, keeping track of their
        left and right values.
    At the end we will return root1
    """
    if not root1:
        return root2
    if not root2:
        return root1
    stack = [(root1, root2)]
    while stack:
        left, right = stack.pop(-1)
        if not left or not right:
            continue
        left.val = left.val + right.val
        if left.left is None:
            left.left = right.left
        else:
            stack.append((left.left, right.left))
        if left.right is None:
            left.right = right.right
        else:
            stack.append((left.right, right.right))
    return root1


"""
Run DETAILS
Runtime: 88 ms, faster than 71.64% of Python3 online submissions for Merge Two Binary Trees.
Memory Usage: 15.4 MB, less than 81.41% of Python3 online submissions for Merge Two Binary Trees.
"""
