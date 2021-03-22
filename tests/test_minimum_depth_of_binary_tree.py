from problems.minimum_depth_of_binary_tree import min_depth, TreeNode


def test_minimum_depth_of_binary_tree_1():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    expected = 2
    actual = min_depth(root)
    assert actual == expected


def test_minimum_depth_of_binary_tree_2():
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    root.right.right.right.right = TreeNode(6)
    expected = 5
    actual = min_depth(root)
    assert actual == expected


def test_minimum_depth_of_binary_tree_3():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(9)
    root.left.left.right = TreeNode(8)
    root.left.left.right.right = TreeNode(12)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.left = TreeNode(10)
    root.right.right.right = TreeNode(11)
    expected = 3
    actual = min_depth(root)
    assert actual == expected


def test_minimum_depth_of_binary_tree_4():
    root = None
    expected = 0
    actual = min_depth(root)
    assert actual == expected
