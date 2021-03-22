"""
Given the head of a singly linked list, return true if it is a palindrome.
"""
from test_utils import ListNode


def _reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def _find_middle(head: ListNode) -> ListNode:
    turtle = hair = head
    while hair is not None and hair.next is not None:
        turtle = turtle.next
        hair = hair.next.next
    return turtle


def is_palindrome(head: ListNode) -> bool:
    """
    Explanation
    Since we are using linked lists we want to try to do this with O(1) extra space. So here is the basic idea
    1. We first find the middle of the list using the fast and slow method
    2. We then reverse the second half of the linked list without losing track of the middle
    3. We then start at the beginning and compare the middle onward to the beginning onward returning false if diff
    4. Reverse the second half again back to the beginning
    5. Return True if we made it this far
    """
    found_middle = _find_middle(head)
    rev_middle = _reverse_list(found_middle)
    front_node = head
    middle_node = rev_middle
    result = True
    while result and middle_node is not None:
        if front_node.val != middle_node.val:
            result = False
        front_node = front_node.next
        middle_node = middle_node.next
    _reverse_list(rev_middle)
    return result


"""
Runtime: 888 ms, faster than 5.18% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 47.3 MB, less than 6.31% of Python3 online submissions for Palindrome Linked List.
"""