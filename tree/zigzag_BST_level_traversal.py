"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/


Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to
right, then right to left for the next level and alternate between).

Example 1:

.. image:: https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
from typing import List, Optional
from tree import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass
