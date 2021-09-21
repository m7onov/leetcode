"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/789/

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be
set to NULL.
Initially, all next pointers are set to NULL.

Example 1:

.. image:: https://assets.leetcode.com/uploads/2019/02/14/116_sample.png

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point
to its next right node, just like in Figure B. The serialized output is in level order as connected by the next
pointers, with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2^12 - 1].
-1000 <= Node.val <= 1000

Follow-up:
You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""
from typing import Optional
from tree import TreeNodeLL
from collections import deque


def connect_branch_by_branch(root: TreeNodeLL) -> TreeNodeLL:
    def connect_margins(left, right):
        left_cur_node = left
        right_cur_node = right
        while left_cur_node is not None and right_cur_node is not None:
            left_cur_node.next = right_cur_node
            left_cur_node = left_cur_node.right
            right_cur_node = right_cur_node.left

    def connect_tree(node: TreeNodeLL):
        if node is None:
            return
        connect_tree(node.left)
        connect_tree(node.right)
        # connect right margin of left subtree to left margin of left subtree
        connect_margins(node.left, node.right)

    connect_tree(root)
    return root


def connect_level_by_level_deque(root: TreeNodeLL) -> Optional[TreeNodeLL]:
    if root is None:
        return None

    dq = deque()
    dq.append(root)
    while len(dq) > 0:
        prev = None
        for i in range(len(dq)):
            cur = dq.popleft()
            if prev is not None:
                prev.next = cur
            if cur.left is not None:
                dq.append(cur.left)
            if cur.right is not None:
                dq.append(cur.right)
            prev = cur
    return root


def connect_level_by_level_no_deque(root: TreeNodeLL) -> Optional[TreeNodeLL]:
    leftmost = root
    while leftmost is not None and leftmost.left is not None:
        prev_node = None
        cur_node = leftmost
        while cur_node is not None:
            if cur_node.left is not None:
                cur_node.left.next = cur_node.right

            if prev_node is not None:
                if prev_node.right is not None:
                    prev_node.right.next = cur_node.left

            prev_node = cur_node
            cur_node = cur_node.next

        leftmost = leftmost.left

    return root


tr = TreeNodeLL(1)
tr.left = TreeNodeLL(2)
tr.right = TreeNodeLL(3)
tr.left.left = TreeNodeLL(4)
tr.left.right = TreeNodeLL(5)
tr.right.left = TreeNodeLL(6)
tr.right.right = TreeNodeLL(7)

# connect_branch_by_branch(tr)
# print(tr.to_full_str())
#
# connect_level_by_level_deque(tr)
# print(tr.to_full_str())

connect_level_by_level_no_deque(tr)
print(tr.to_full_str())
