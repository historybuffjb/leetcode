from problems.binary_tree_zigzag_level_order_traversal import (
    TreeNode,
    zig_zag_level_order,
)


def test_binary_tree_zigzag_level_order_traversal_1():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    expected = [[3], [20, 9], [15, 7]]
    actual = zig_zag_level_order(root)
    assert actual == expected


def test_binary_tree_zigzag_level_order_traversal_2():
    root = TreeNode(1)
    expected = [[1]]
    actual = zig_zag_level_order(root)
    assert actual == expected


def test_binary_tree_zigzag_level_order_traversal_3():
    root = None
    expected = []
    actual = zig_zag_level_order(root)
    assert actual == expected


def test_binary_tree_zigzag_level_order_traversal_4():
    root = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(4, TreeNode(8), TreeNode(9)),
            TreeNode(5, TreeNode(10), TreeNode(11)),
        ),
        TreeNode(3, TreeNode(6, None, TreeNode(13)), TreeNode(7, TreeNode(14))),
    )
    expected = [[1], [3, 2], [4, 5, 6, 7], [14, 13, 11, 10, 9, 8]]
    actual = zig_zag_level_order(root)
    assert actual == expected
