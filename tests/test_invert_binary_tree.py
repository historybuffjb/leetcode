from problems.invert_binary_tree import invert_tree, TreeNode
from test_utils import compare_tree_nodes

DEBUG = False


def test_invert_binary_tree_1():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    expected = TreeNode(4)
    expected.left = TreeNode(7)
    expected.right = TreeNode(2)
    expected.left.left = TreeNode(9)
    expected.left.right = TreeNode(6)
    expected.right.left = TreeNode(3)
    expected.right.right = TreeNode(1)
    actual = invert_tree(root)
    assert compare_tree_nodes(expected, actual, DEBUG) is True


def test_invert_binary_tree_2():
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    expected = TreeNode(4)
    expected.left = TreeNode(3)
    expected.right = TreeNode(1)
    actual = invert_tree(root)
    assert compare_tree_nodes(expected, actual, DEBUG) is True


def test_invert_binary_tree_3():
    root = None
    expected = None
    actual = invert_tree(root)
    assert compare_tree_nodes(expected, actual, DEBUG) is True
