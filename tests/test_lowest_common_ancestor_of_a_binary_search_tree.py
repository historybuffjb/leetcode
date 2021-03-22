from problems.lowest_common_ancestor_of_a_binary_search_tree import lowest_common_ancestor, TreeNode


def test_lowest_common_ancestor_of_a_binary_search_tree_1():
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    p = root.left
    q = root.right
    expected = root
    actual = lowest_common_ancestor(root, p, q)
    assert actual == expected


def test_lowest_common_ancestor_of_a_binary_search_tree_2():
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    p = root.left
    q = root.left.right
    expected = root.left
    actual = lowest_common_ancestor(root, p, q)
    assert actual == expected


def test_lowest_common_ancestor_of_a_binary_search_tree_3():
    root = TreeNode(2)
    root.left = TreeNode(1)
    p = root
    q = root.left
    expected = root
    actual = lowest_common_ancestor(root, p, q)
    assert actual == expected
