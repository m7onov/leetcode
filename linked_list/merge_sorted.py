"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/771/

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the
nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nx=None):
        self.val = val
        self.next = nx


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    new_list_head = ListNode()
    new_list_curr = new_list_head

    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            new_list_curr.next = l1
            new_list_curr = new_list_curr.next
            l1 = l1.next
        else:
            new_list_curr.next = l2
            new_list_curr = new_list_curr.next
            l2 = l2.next

    if l1 is not None:
        new_list_curr.next = l1
    elif l2 is not None:
        new_list_curr.next = l2
    else:
        new_list_curr.next = None

    return new_list_head.next

