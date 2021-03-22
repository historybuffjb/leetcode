from problems.subtree_of_another_tree import is_subtree, TreeNode


def test_subtree_of_another_tree_1():
    s = TreeNode(3)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(2)
    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(2)
    expected = True
    actual = is_subtree(s, t)
    assert actual == expected


def test_subtree_of_another_tree_2():
    s = TreeNode(3)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(2)
    s.left.right.left = TreeNode(0)
    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(2)
    expected = False
    actual = is_subtree(s, t)
    assert actual == expected


def test_subtree_of_another_tree_3():
    s = TreeNode(3)
    t = TreeNode(3)
    expected = True
    actual = is_subtree(s, t)
    assert actual == expected


def test_subtree_of_another_tree_4():
    s = TreeNode(3)
    t = TreeNode(4)
    expected = False
    actual = is_subtree(s, t)
    assert actual == expected


def test_subtree_of_another_tree_5():
    s = TreeNode(3)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(2)
    s.left.right.left = TreeNode(0)
    t = TreeNode(3)
    t.left = TreeNode(4)
    t.right = TreeNode(5)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(2)
    t.left.right.left = TreeNode(0)
    expected = True
    actual = is_subtree(s, t)
    assert actual == expected
