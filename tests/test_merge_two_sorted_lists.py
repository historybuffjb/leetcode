from problems.merge_two_sorted_lists import ListNode, merge_two_lists
from test_utils import compare_list_nodes

DEBUG = False


def test_merge_two_sorted_lists_1():
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    expected = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
    actual = merge_two_lists(l1, l2)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_merge_two_sorted_lists_2():
    l1 = None
    l2 = None
    expected = None
    actual = merge_two_lists(l1, l2)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_merge_two_sorted_lists_3():
    l1 = None
    l2 = ListNode(0)
    expected = ListNode(0)
    actual = merge_two_lists(l1, l2)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_merge_two_sorted_lists_4():
    l1 = ListNode(0)
    l2 = None
    expected = ListNode(0)
    actual = merge_two_lists(l1, l2)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_merge_two_sorted_lists_5():
    l1 = ListNode(-42, ListNode(-0, ListNode(1, ListNode(7, ListNode(37, ListNode(42, ListNode(49, ListNode(52))))))))
    l2 = ListNode(-71, ListNode(-52, ListNode(-21, ListNode(4, ListNode(10, ListNode(41, ListNode(55, ListNode(100))))))))
    expected = ListNode(-71, ListNode(-52, ListNode(-42, ListNode(-21, ListNode(0, ListNode(1, ListNode(4, ListNode(7, ListNode(10, ListNode(37, ListNode(41, ListNode(42, ListNode(49, ListNode(52, ListNode(55, ListNode(100))))))))))))))))
    actual = merge_two_lists(l1, l2)
    assert compare_list_nodes(expected, actual, DEBUG) is True
