from problems.merge_two_binary_trees import merge_trees, TreeNode
from test_utils import compare_tree_nodes

DEBUG = True


def test_merge_two_binary_trees_1():
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.left.right = TreeNode(4)
    root2.right = TreeNode(3)
    root2.right.right = TreeNode(7)
    expected = TreeNode(3)
    expected.left = TreeNode(4)
    expected.left.left = TreeNode(5)
    expected.left.right = TreeNode(4)
    expected.right = TreeNode(5)
    expected.right.right = TreeNode(7)
    actual = merge_trees(root1, root2)
    assert compare_tree_nodes(expected, actual, DEBUG) is True


def test_merge_two_binary_trees_2():
    root1 = TreeNode(1)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    expected = TreeNode(2)
    expected.left = TreeNode(2)
    actual = merge_trees(root1, root2)
    assert compare_tree_nodes(expected, actual, DEBUG) is True


def test_merge_two_binary_trees_3():
    root1 = None
    root2 = TreeNode(1)
    expected = TreeNode(1)
    actual = merge_trees(root1, root2)
    assert compare_tree_nodes(expected, actual, DEBUG) is True


def test_merge_two_binary_trees_4():
    root1 = TreeNode(1)
    root2 = None
    expected = TreeNode(1)
    actual = merge_trees(root1, root2)
    assert compare_tree_nodes(expected, actual, DEBUG) is True


def test_merge_two_binary_trees_5():
    root1 = TreeNode(1)
    root2 = TreeNode(1)
    expected = TreeNode(2)
    actual = merge_trees(root1, root2)
    assert compare_tree_nodes(expected, actual, DEBUG) is True


def test_merge_two_binary_trees_6():
    root1 = None
    root2 = None
    expected = None
    actual = merge_trees(root1, root2)
    assert compare_tree_nodes(expected, actual, DEBUG) is True
