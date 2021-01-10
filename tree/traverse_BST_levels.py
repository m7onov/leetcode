"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/628/

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from typing import List
from tree import TreeNode


def level_order(root: TreeNode) -> List[List[int]]:
    if root is None:
        return []

    level_vals = [[root.val]]
    prev_level = [root]
    while len(prev_level) > 0:
        next_level_vals = []
        next_level = []
        for node in prev_level:
            if node.left is not None:
                next_level.append(node.left)
                next_level_vals.append(node.left.val)

            if node.right is not None:
                next_level.append(node.right)
                next_level_vals.append(node.right.val)

        prev_level = next_level
        if len(next_level_vals) > 0:
            level_vals.append(next_level_vals)

    return level_vals


def test1():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(level_order(root))


test1()
