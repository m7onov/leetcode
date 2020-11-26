"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/603/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nx=None):
        self.val = val
        self.next = nx


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    sz = 0
    node = head
    while node is not None:
        node = node.next
        sz += 1

    if sz == n:
        return head.next

    prev = None
    node = head
    for i in range(sz - n):
        prev = node
        node = node.next

    prev.next = node.next
    return head
