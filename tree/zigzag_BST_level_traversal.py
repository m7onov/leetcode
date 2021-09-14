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
from collections import defaultdict


class Solution:
    def inorder_traversal(self, level_idx, root, cb):
        if root is None:
            return
        if root.left is not None:
            self.inorder_traversal(level_idx + 1, root.left, cb)
        cb(level_idx, root)
        if root.right is not None:
            self.inorder_traversal(level_idx + 1, root.right, cb)

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = defaultdict(list)

        def traverse_cb(level_idx, node):
            if level_idx % 2 == 0:
                ret[level_idx].append(node.val)
            else:
                ret[level_idx].insert(0, node.val)

        self.inorder_traversal(0, root, traverse_cb)

        return [ret[i] for i in sorted(ret.keys())]


sol = Solution()
tr = TreeNode(3)
tr.left = TreeNode(9)
tr.right = TreeNode(20)
tr.left.left = TreeNode(15)
tr.left.right = TreeNode(7)
ans = sol.zigzagLevelOrder(tr)
print(ans)

tr = TreeNode(1)
ans = sol.zigzagLevelOrder(tr)
print(ans)

tr = None
ans = sol.zigzagLevelOrder(tr)
print(ans)
