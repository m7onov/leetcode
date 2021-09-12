"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/784/

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even
indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:

.. image:: https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:

.. image:: https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints:
n == number of nodes in the linked list
0 <= n <= 10^4
-10^6 <= Node.val <= 10^6
"""
from typing import Optional
from linked_list import ListNode, make_linked_list_from_list


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_tail = head
        even_head = odd_tail.next if odd_tail is not None else None
        even_tail = even_head
        while even_tail is not None and even_tail.next is not None:
            odd_tail.next = even_tail.next
            odd_tail = odd_tail.next
            if odd_tail is not None:
                even_tail.next = odd_tail.next
                even_tail = even_tail.next

        if odd_tail is not None:
            odd_tail.next = even_head

        return head


sol = Solution()
sol.oddEvenList(make_linked_list_from_list([1, 2, 3, 4, 5, 6]))
sol.oddEvenList(make_linked_list_from_list([]))
sol.oddEvenList(make_linked_list_from_list([1]))
sol.oddEvenList(make_linked_list_from_list([1, 2]))
