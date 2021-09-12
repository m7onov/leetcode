"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

.. image:: https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional
from linked_list import ListNode, make_linked_list_from_number


class Solution:
    # O(L) - speed; L is maximum length of l1 or l2
    # O(L) - memory; L is maximum length of l1 or l2
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        rp = None
        carrying = 0
        while l1 is not None or l2 is not None:
            s = carrying
            carrying = 0
            if l1 is not None:
                s += l1.val
                l1 = l1.next
            if l2 is not None:
                s += l2.val
                l2 = l2.next

            if s > 9:
                carrying = 1

            if rp is None:
                rp = result
            else:
                rp.next = ListNode()
                rp = rp.next

            rp.val = s % 10

        if carrying == 1:
            rp.next = ListNode(1)

        return result


sol = Solution()
res = sol.addTwoNumbers(make_linked_list_from_number(342), make_linked_list_from_number(465))
print(res)

res = sol.addTwoNumbers(make_linked_list_from_number(0), make_linked_list_from_number(0))
print(res)

res = sol.addTwoNumbers(make_linked_list_from_number(9999999), make_linked_list_from_number(9999))
print(res)
