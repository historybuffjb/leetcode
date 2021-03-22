from problems.merge_k_sorted_lists import ListNode, merge_k_lists
from test_utils import compare_list_nodes

DEBUG = False


def test_merge_k_sorted_lists_1():
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    lists = [l1, l2, l3]
    expected = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))
    actual = merge_k_lists(lists)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_merge_k_sorted_lists_2():
    lists = []
    expected = None
    actual = merge_k_lists(lists)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_merge_k_sorted_lists_3():
    lists = [None]
    expected = None
    actual = merge_k_lists(lists)
    assert compare_list_nodes(expected, actual, DEBUG) is True
