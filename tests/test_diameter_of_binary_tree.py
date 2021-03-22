from problems.diameter_of_binary_tree import diameter_of_binary_tree, TreeNode


def test_diameter_of_binary_tree_1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    expected = 3
    actual = diameter_of_binary_tree(root)
    assert actual == expected


def test_diameter_of_binary_tree_2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    expected = 1
    actual = diameter_of_binary_tree(root)
    assert actual == expected


def test_diameter_of_binary_tree_3():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    expected = 6
    actual = diameter_of_binary_tree(root)
    assert actual == expected


def test_diameter_of_binary_tree_4():
    root = TreeNode(5)
    expected = 0
    actual = diameter_of_binary_tree(root)
    assert actual == expected


def test_diameter_of_binary_tree_5():
    root = TreeNode(5)
    root.left = TreeNode(7)
    root.left.left = TreeNode(9)
    root.left.left.left = TreeNode(11)
    root.left.left.left.left = TreeNode(13)
    root.left.left.left.left.left = TreeNode(15)
    root.right = TreeNode(9)
    expected = 6
    actual = diameter_of_binary_tree(root)
    assert actual == expected
