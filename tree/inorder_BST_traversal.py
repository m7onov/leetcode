"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/786/

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

.. image:: https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:

.. image:: https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg

Input: root = [1,2]
Output: [2,1]

Example 5:

.. image:: https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg

Input: root = [1,null,2]
Output: [1,2]


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import Optional, List
from tree import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Note: look at contest_dec_2020/week2/03_bst_inorder_iterator.py
        pass
