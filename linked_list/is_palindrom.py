"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/772/

Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nx=None):
        self.val = val
        self.next = nx


def reverse_half_of_list_iteratively(head: ListNode, list_size: int) -> (ListNode, ListNode):
    new_head = head
    cut = new_head.next
    new_head.next = None
    for i in range(list_size // 2 - 1):
        nx = cut.next
        cut.next = new_head
        new_head = cut
        cut = nx

    return new_head, cut


def is_palindrome(head: ListNode) -> bool:
    if head is None or head.next is None:
        return True

    # size of list?
    node = head
    list_size = 0
    while node is not None:
        list_size += 1
        node = node.next

    # half_1 size <= half_2 size (in case of odd list_size)
    half_1, half_2 = reverse_half_of_list_iteratively(head, list_size)
    if list_size % 2 == 1:
        half_2 = half_2.next

    while half_1 is not None:
        if half_1.val != half_2.val:
            return False

        half_1 = half_1.next
        half_2 = half_2.next

    return True

