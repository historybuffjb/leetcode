"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
"""
# Definition for singly-linked list.
import heapq
from typing import List

from test_utils import ListNode


def _merge_two_linked_lists(l1: ListNode, l2: ListNode) -> ListNode:
    root = temp = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    if not l1:
        temp.next = l2
    else:
        temp.next = l1
    return root.next


def merge_k_lists(lists: List[ListNode]) -> ListNode:
    """
    Explanation
    The best way to do this is to divide and conquer. We merge the linked lists two at a time, collapsing down
    until eventually we merge the last two arrays.
    """
    if len(lists) == 0:
        return None
    current = 1
    while current < len(lists):
        for i in range(0, len(lists) - current, current * 2):
            lists[i] = _merge_two_linked_lists(lists[i], lists[i + current])
        current *= 2
    return lists[0]


"""
Run DETAILS
Runtime: 112 ms, faster than 53.93% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.8 MB, less than 82.25% of Python3 online submissions for Merge k Sorted Lists.
"""
