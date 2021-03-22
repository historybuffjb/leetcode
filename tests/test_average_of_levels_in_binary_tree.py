from problems.average_of_levels_in_binary_tree import average_of_levels, TreeNode
from test_utils import compare_lists


def test_average_of_levels_in_binary_tree_1():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    expected = [3.0, 14.5, 11.0]
    actual = average_of_levels(root)
    assert compare_lists(expected, actual) is True


def test_average_of_levels_in_binary_tree_2():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = TreeNode(15)
    root.left.right = TreeNode(7)
    root.right = TreeNode(20)
    expected = [3.0, 14.5, 11.0]
    actual = average_of_levels(root)
    assert compare_lists(expected, actual) is True
