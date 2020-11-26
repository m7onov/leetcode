"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/560/

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nx=None):
        self.val = val
        self.next = nx


def reverse_list_iteratively(head: ListNode) -> ListNode:
    new_head = head
    cut = new_head.next
    new_head.next = None
    while cut is not None:
        nx = cut.next
        cut.next = new_head
        new_head = cut
        cut = nx

    return new_head


def reverse_list_recursion_smart(head: ListNode) -> ListNode:
    if head.next is None:
        return head
    else:
        new_head = reverse_list_recursion_smart(head.next)
        head.next.next = head
        head.next = None
        return new_head


def reverse_list_recursively(self, head: ListNode) -> ListNode:
    return self.reverse_list_recursion_smart(head)


def reverse_list(head: ListNode) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    return reverse_list_iteratively(head)
    # return self.reverse_list_recursively(head)
