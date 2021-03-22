"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as
a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
from test_utils import ListNode


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
   EXPLANATION:
      * Get the longest list then:
      * Loop through the longest list until both l1 nad l2 are null and do the following:
         * Sum l1 val and l2 val (if they exist) and add remainder
         * remainder is sum / 10
         * create node of sum
         * set node to next
      * At the end check if there is still a remainder:
         * if so create a list element with that and append
      * Return head of nodes
   """
    result = ListNode()
    traverser = result
    remainder = 0
    while l1 or l2:
        temp_sum = remainder
        temp_sum += l1.val if l1 else 0
        temp_sum += l2.val if l2 else 0
        remainder = temp_sum // 10
        traverser.next = ListNode(temp_sum % 10)
        traverser = traverser.next
        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2
    if remainder != 0:
        traverser.next = ListNode(1)
    return result.next


"""
RUN DETAILS
Runtime: 64 ms, faster than 89.44% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.3 MB, less than 45.04% of Python3 online submissions for Add Two Numbers.
"""
