from problems.reverse_linked_list import reverse_list, ListNode
from test_utils import compare_list_nodes

DEBUG = False


def test_reverse_linked_list_1():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    expected = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
    actual = reverse_list(head)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_reverse_linked_list_2():
    head = ListNode(1, ListNode(2))
    expected = ListNode(2, ListNode(1))
    actual = reverse_list(head)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_reverse_linked_list_3():
    head = None
    expected = None
    actual = reverse_list(head)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_reverse_linked_list_4():
    head = ListNode(1)
    expected = ListNode(1)
    actual = reverse_list(head)
    assert compare_list_nodes(expected, actual, DEBUG) is True
