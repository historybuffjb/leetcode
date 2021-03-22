"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from test_utils import ListNode


def reverse_list(head: ListNode) -> ListNode:
    """
    Explanation
    The idea here is to swap our curr node's next pointer with the previous node's pointer. Thus the solution
    is pretty obvious.
    """
    prev = None
    curr = head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


"""
Run DETAILS
Runtime: 36 ms, faster than 69.43% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.4 MB, less than 99.55% of Python3 online submissions for Reverse Linked List.
"""