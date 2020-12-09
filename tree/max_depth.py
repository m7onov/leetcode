"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/555/

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def max_depth_recursive_dumb(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        left_depth = 0
        right_depth = 0

        if root.left is not None:
            left_depth = self.max_depth_recursive_dumb(root.left) + 1

        if root.right is not None:
            right_depth = self.max_depth_recursive_dumb(root.right) + 1

        return max(left_depth, right_depth)

    def max_depth_recursive_simple(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_depth = self.max_depth_recursive_simple(root.left) + 1
        right_depth = self.max_depth_recursive_simple(root.right) + 1

        return max(left_depth, right_depth)

    def max_depth(self, root: TreeNode) -> int:
        return self.max_depth_recursive_simple(root)
