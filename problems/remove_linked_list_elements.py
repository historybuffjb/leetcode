"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
and return the new head.
"""
from test_utils import ListNode


def remove_elements(head: ListNode, val: int) -> ListNode:
    """
    Explanation
    Since we are removing elements from a single-chained linked list, we need to keep track of where we were
    previously, and where we are now. So we can use a turtle and hair approach where the hair is always one step ahead.
    """
    final = ListNode()
    final.next = head
    prev = final
    curr = head
    while curr is not None:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return final.next


"""
Run DETAILS
Runtime: 72 ms, faster than 51.15% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 17.3 MB, less than 25.82% of Python3 online submissions for Remove Linked List Elements.
"""