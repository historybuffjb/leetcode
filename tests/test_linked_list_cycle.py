from problems.linked_list_cycle import has_cycle, ListNode
from test_utils import compare_list_nodes


def test_linked_list_cycle_1():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next
    expected = True
    actual = has_cycle(head)
    assert actual == expected


def test_linked_list_cycle_2():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    expected = True
    actual = has_cycle(head)
    assert actual == expected


def test_linked_list_cycle_3():
    head = ListNode(1)
    expected = False
    actual = has_cycle(head)
    assert actual == expected


def test_linked_list_cycle_4():
    head = None
    expected = False
    actual = has_cycle(head)
    assert actual == expected


def test_linked_list_cycle_5():
    head = ListNode(1)
    head.next = head
    expected = True
    actual = has_cycle(head)
    assert actual == expected
