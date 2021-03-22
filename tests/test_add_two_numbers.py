# Tests for Add Two Numbers

from problems.add_two_numbers import add_two_numbers
from test_utils import compare_list_nodes, ListNode

DEBUG = False


def test_add_two_numbers_1():
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    expected = ListNode(7, ListNode(0, ListNode(8)))
    actual = add_two_numbers(l1, l2)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_add_two_numbers_2():
    l1 = ListNode(0)
    l2 = ListNode(0)
    expected = ListNode(0)
    actual = add_two_numbers(l1, l2)
    assert compare_list_nodes(expected, actual, DEBUG) is True


def test_add_two_numbers_3():
    l1 = ListNode(
        9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
    )
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    expected = ListNode(
        8,
        ListNode(
            9,
            ListNode(
                9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1)))))
            ),
        ),
    )
    actual = add_two_numbers(l1, l2)
    assert compare_list_nodes(expected, actual, DEBUG) is True
