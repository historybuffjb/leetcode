from problems.middle_of_the_linked_list import middle_node, ListNode
from test_utils import compare_list_nodes

DEBUG = False


def test_middle_of_the_linked_list_1():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    expected = head.next.next
    actual = middle_node(head)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_middle_of_the_linked_list_2():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    expected = head.next.next.next
    actual = middle_node(head)
    assert compare_list_nodes(expected, actual, DEBUG) is True
