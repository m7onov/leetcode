"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3566/

Given a non-negative integer represented as a linked list of digits, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list.

Example 1:
Input: head = [1,2,3]
Output: [1,2,4]

Example 2:
Input: head = [0]
Output: [1]

Constraints:
The number of nodes in the linked list is in the range [1, 100].
0 <= Node.val <= 9
The number represented by the linked list does not contain leading zeros except for the zero itself.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + '->' + str(self.next)

    def __repr__(self):
        return self.__str__()


def plus_one(head: ListNode):
    last_not_9_node = None
    overflow_head = head
    while overflow_head is not None:
        if overflow_head.val != 9:
            last_not_9_node = overflow_head

        overflow_head = overflow_head.next

    if last_not_9_node is None:
        last_not_9_node = ListNode(1)
        last_not_9_node.next = head
        overflow_head = head
        head = last_not_9_node

    else:
        last_not_9_node.val += 1
        overflow_head = last_not_9_node.next

    while overflow_head is not None:
        overflow_head.val = 0
        overflow_head = overflow_head.next

    return head


# a = [9, 9, 9, 9, 9, 9]
# a = [9, 9, 9, 5, 9, 9]
# a = [9, 9, 9, 5, 9, 0]
# a = [0]
a = [8, 9, 9, 9]
_node = _head = ListNode(a[0])
for i in a[1:]:
    _node.next = ListNode(i)
    _node = _node.next

print(plus_one(_head))
