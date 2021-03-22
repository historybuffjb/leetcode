from problems.maximum_depth_of_binary_tree import max_depth, TreeNode


def test_maximum_depth_of_binary_tree_1():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    expected = 3
    actual = max_depth(root)
    assert actual == expected


def test_maximum_depth_of_binary_tree_2():
    root = TreeNode(1)
    root.right = TreeNode(2)
    expected = 2
    actual = max_depth(root)
    assert actual == expected


def test_maximum_depth_of_binary_tree_3():
    root = None
    expected = 0
    actual = max_depth(root)
    assert actual == expected


def test_maximum_depth_of_binary_tree_4():
    root = TreeNode(0)
    expected = 1
    actual = max_depth(root)
    assert actual == expected


def test_maximum_depth_of_binary_tree_5():
    root = TreeNode(0)
    root.right = TreeNode(1)
    root.right.right = TreeNode(2)
    root.right.right.right = TreeNode(3)
    root.right.right.right.right = TreeNode(4)
    expected = 5
    actual = max_depth(root)
    assert actual == expected
