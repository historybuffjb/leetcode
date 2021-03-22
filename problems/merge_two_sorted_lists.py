"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing
together the nodes of the first two lists.
"""
from test_utils import ListNode


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Explanation
    Since the lists are already sorted, this should be pretty easy. The basic idea is to create an empty.
    We then loop through l1 and l2 until we have reached the end of both. We can then return our created.next
    """
    final = ListNode()
    temp = final
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    temp.next = l1 if l1 is not None else l2
    return final.next


"""
Run DETAILS
Runtime: 36 ms, faster than 76.54% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 14.2 MB, less than 64.11% of Python3 online submissions for Merge Two Sorted Lists.
"""
