"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

.. image:: https://assets.leetcode.com/uploads/2021/03/05/160_statement.png

The test cases are generated such that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns.

Custom Judge:
The inputs to the judge are given as follows (your program is not given these inputs):
    - intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
    - listA - The first linked list.
    - listB - The second linked list.
    - skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
    - skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your
program. If you correctly return the intersected node, then your solution will be accepted.

Example 1:

.. image:: https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:

.. image:: https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png

Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:

.. image:: https://assets.leetcode.com/uploads/2021/03/05/160_example_3.png

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Constraints:
    - The number of nodes of listA is in the m.
    - The number of nodes of listB is in the n.
    - 0 <= m, n <= 3 * 104
    - 1 <= Node.val <= 105
    - 0 <= skipA <= m
    - 0 <= skipB <= n
    - intersectVal is 0 if listA and listB do not intersect.
    - intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

Follow up: Could you write a solution that runs in O(n) time and use only O(1) memory?
"""
from linked_list import ListNode, make_linked_list_from_list, get_by_index


class Solution:
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == headB:
            return headA

        cur_node = headA
        while cur_node is not None:
            cur_node.val = -cur_node.val
            cur_node = cur_node.next

        result = None
        cur_node = headB
        while cur_node is not None:
            if cur_node.val < 0:
                result = cur_node
                break
            cur_node = cur_node.next

        cur_node = headA
        while cur_node is not None:
            cur_node.val = -cur_node.val
            cur_node = cur_node.next

        cur_node = headB
        while cur_node is not None:
            if cur_node.val < 0:
                cur_node.val = -cur_node.val
                cur_node = cur_node.next
            else:
                break

        return result


    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        def list_sign(l: ListNode, v: str):
            c = l
            while c is not None:
                if v == '+':
                    c.val = abs(c.val)
                else:
                    c.val = -abs(c.val)
                c = c.next

        list_sign(headA, '-')

        result = headB
        cur_node = headB
        while cur_node is not None:
            if cur_node.val < 0:
                result = cur_node
                break
            cur_node = cur_node.next

        if cur_node is None:
            result = None

        list_sign(headA, '+')
        list_sign(headB, '+')
        return result

    # the best one; without trick of negating values
    def getIntersectionNode3(self, headA: ListNode, headB: ListNode) -> ListNode:
        def get_linked_list_len(head):
            cur_node = head
            ll_len = 0
            while cur_node is not None:
                ll_len += 1
                cur_node = cur_node.next
            return ll_len

        def move_to_index(head, idx):
            while idx > 0:
                head = head.next
                idx -= 1
            return head

        len_a = get_linked_list_len(headA)
        len_b = get_linked_list_len(headB)

        start_a = headA
        start_b = headB
        if len_a < len_b:
            start_b = move_to_index(headB, len_b - len_a)
        elif len_b < len_a:
            start_a = move_to_index(headA, len_a - len_b)

        # now start_a and start_b lists have the same length
        while start_a is not None and start_a != start_b:
            start_a = start_a.next
            start_b = start_b.next

        return start_a


sol = Solution()

a = make_linked_list_from_list([4, 1, 8, 4, 5])
b = make_linked_list_from_list([5, 6, 1, 8, 4, 5])
get_by_index(a, 1).next = get_by_index(b, 3)
print(f'a: {a}')
print(f'b: {b}')
print('intersection:', sol.getIntersectionNode3(a, b))
#
print('--------------')
#
a = make_linked_list_from_list([1])
b = a
print(f'a: {a}')
print(f'b: {b}')
print('intersection:', sol.getIntersectionNode3(a, b))
#
print('--------------')
#
a = make_linked_list_from_list([1, 2])
b = make_linked_list_from_list([2])
get_by_index(a, 0).next = get_by_index(b, 0)
print(f'a: {a}')
print(f'b: {b}')
print(sol.getIntersectionNode3(a, b))
#
print('--------------')
#
a = make_linked_list_from_list([2, 6, 4])
b = make_linked_list_from_list([1, 5])
print(f'a: {a}')
print(f'b: {b}')
print(sol.getIntersectionNode3(a, b))
