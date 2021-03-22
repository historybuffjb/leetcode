"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
"""
from test_utils import ListNode


def delete_duplicates(head: ListNode) -> ListNode:
    """
    Explanation
    The first thing to notice is that each sorted number could have multiple duplicates. This informs how we solve.
    1. The first thing to do is to keep a prev and current node as we traverse through the list.
    2. Thus we can just check if the current val and next val are equal. If show, set current next to current next next
    3. Return head
    """
    curr = head
    while curr is not None and curr.next is not None:
        if curr.next.val == curr.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


"""
Run DETAILS
Runtime: 44 ms, faster than 58.34% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 14.1 MB, less than 95.38% of Python3 online submissions for Remove Duplicates from Sorted List.
"""
