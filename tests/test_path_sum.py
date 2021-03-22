from problems.path_sum import has_path_sum, TreeNode


def test_path_sum_1():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    target_sum = 22
    expected = True
    actual = has_path_sum(root, target_sum)
    assert actual == expected


def test_path_sum_2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    target_sum = 5
    expected = False
    actual = has_path_sum(root, target_sum)
    assert actual == expected


def test_path_sum_3():
    root = TreeNode(1)
    root.left = TreeNode(2)
    target_sum = 0
    expected = False
    actual = has_path_sum(root, target_sum)
    assert actual == expected


def test_path_sum_4():
    root = TreeNode(1)
    target_sum = 1
    expected = True
    actual = has_path_sum(root, target_sum)
    assert actual == expected


def test_path_sum_5():
    root = None
    target_sum = 1
    expected = False
    actual = has_path_sum(root, target_sum)
    assert actual == expected
