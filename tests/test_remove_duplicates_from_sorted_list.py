from problems.remove_duplicates_from_sorted_list import delete_duplicates, ListNode
from test_utils import compare_list_nodes

DEBUG = False


def test_remove_duplicates_from_sorted_list_1():
    head = ListNode(1, ListNode(1, ListNode(2)))
    expected = ListNode(1, ListNode(2))
    actual = delete_duplicates(head)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_remove_duplicates_from_sorted_list_2():
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    expected = ListNode(1, ListNode(2, ListNode(3)))
    actual = delete_duplicates(head)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_remove_duplicates_from_sorted_list_3():
    head = None
    expected = None
    actual = delete_duplicates(head)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_remove_duplicates_from_sorted_list_4():
    head = ListNode(8)
    expected = ListNode(8)
    actual = delete_duplicates(head)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_remove_duplicates_from_sorted_list_5():
    head = ListNode(-53, ListNode(-23, ListNode(-23, ListNode(-17, ListNode(-1, ListNode(4, ListNode(4, ListNode(17, ListNode(65, ListNode(78, ListNode(78, ListNode(99, ListNode(100)))))))))))))
    expected = ListNode(-53, ListNode(-23, ListNode(-17, ListNode(-1, ListNode(4, ListNode(17, ListNode(65, ListNode(78, ListNode(99, ListNode(100))))))))))
    actual = delete_duplicates(head)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_remove_duplicates_from_sorted_list_6():
    head = ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(3, ListNode(3, ListNode(3, ListNode(3, ListNode(3, ListNode(3)))))))))))))))
    expected = ListNode(1, ListNode(2, ListNode(3)))
    actual = delete_duplicates(head)
    assert compare_list_nodes(expected, actual, DEBUG) is True
