"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer. Internally, pos is used to denote the
index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""
from test_utils import ListNode


def has_cycle(head: ListNode) -> bool:
    """
    Explanation
    Keep a dictionary of all address pointers for nodes.
    If we ever find a node in the dictionary return True
    Else at the end we return False
    """
    address_pointers = {}
    while head:
        if id(head) in address_pointers:
            return True
        address_pointers[id(head)] = None
        head = head.next
    return False


"""
Runtime: 60 ms, faster than 32.37% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.9 MB, less than 5.45% of Python3 online submissions for Linked List Cycle.
"""