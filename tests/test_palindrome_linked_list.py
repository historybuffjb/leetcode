from problems.palindrome_linked_list import is_palindrome, ListNode


def test_palindrome_linked_list_1():
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    expected = True
    actual = is_palindrome(head)
    assert actual == expected


def test_palindrome_linked_list_2():
    head = ListNode(1, ListNode(2))
    expected = False
    actual = is_palindrome(head)
    assert actual == expected


def test_palindrome_linked_list_3():
    head = ListNode(1)
    expected = True
    actual = is_palindrome(head)
    assert actual == expected


def test_palindrome_linked_list_4():
    head = ListNode(1, ListNode(2, ListNode(1)))
    expected = True
    actual = is_palindrome(head)
    assert actual == expected
