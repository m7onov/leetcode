"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3551/

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest
leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def max_depth(root: TreeNode) -> int:
    if root is None:
        return 0

    left_depth = 1
    right_depth = 1

    if root.left is not None:
        left_depth = max_depth(root.left) + 1

    if root.right is not None:
        right_depth = max_depth(root.right) + 1

    return max(left_depth, right_depth)

