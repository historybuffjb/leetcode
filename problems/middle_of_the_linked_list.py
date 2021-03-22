"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
"""
from test_utils import ListNode


def middle_node(head: ListNode) -> ListNode:
    """
    Explanation
    We could just loop through all the nodes putting their memory addresses in a list. Then we just get the median of
    the list. But here we can use the turtle and the hair approach and have a fast pointer and a slow pointer. The
    fast pointer moves twice as fast as the slow pointer and thus when the fast pointer reaches the end the slow pointer
    should be in the middle.
    """
    turtle = hair = head
    while hair and hair.next:
        turtle = turtle.next
        hair = hair.next.next
    return turtle


"""
Run DETAILS
Runtime: 28 ms, faster than 83.72% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 14.2 MB, less than 76.47% of Python3 online submissions for Middle of the Linked List.
"""
