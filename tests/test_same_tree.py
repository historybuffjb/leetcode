from problems.same_tree import is_same_tree, TreeNode


def test_same_tree_1():
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    expected = True
    actual = is_same_tree(p, q)
    assert actual == expected


def test_same_tree_2():
    p = TreeNode(1)
    p.left = TreeNode(2)
    q = TreeNode(1)
    q.right = TreeNode(2)
    expected = False
    actual = is_same_tree(p, q)
    assert actual == expected


def test_same_tree_3():
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)
    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)
    expected = False
    actual = is_same_tree(p, q)
    assert actual == expected


def test_same_tree_4():
    p = TreeNode(1)
    q = TreeNode(1)
    expected = True
    actual = is_same_tree(p, q)
    assert actual == expected


def test_same_tree_5():
    p = TreeNode(1)
    p.right = TreeNode(2)
    q = TreeNode(1)
    q.right = TreeNode(2)
    expected = True
    actual = is_same_tree(p, q)
    assert actual == expected


def test_same_tree_6():
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.left.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    expected = False
    actual = is_same_tree(p, q)
    assert actual == expected
