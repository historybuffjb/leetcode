from problems.remove_linked_list_elements import remove_elements, ListNode
from test_utils import compare_list_nodes

DEBUG = False


def test_remove_linked_list_elements_1():
    head = ListNode(
        1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    )
    val = 6
    expected = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    actual = remove_elements(head, val)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_remove_linked_list_elements_2():
    head = None
    val = 1
    expected = None
    actual = remove_elements(head, val)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_remove_linked_list_elements_3():
    head = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
    val = 7
    expected = None
    actual = remove_elements(head, val)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_remove_linked_list_elements_4():
    head = ListNode(1)
    val = 5
    expected = ListNode(1)
    actual = remove_elements(head, val)
    assert compare_list_nodes(expected, actual, DEBUG) is True
