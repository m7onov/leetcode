"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/631/

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


def sorted_array_to_bst(nums: List[int]) -> TreeNode:
    nums_len = len(nums)
    root_idx = nums_len // 2

    if nums_len == 0:
        return None
    elif nums_len == 1:
        return TreeNode(nums[0])
    elif nums_len == 2:
        return TreeNode(nums[1], TreeNode(nums[0]))
    elif nums_len == 3:
        return TreeNode(nums[1], TreeNode(nums[0]), TreeNode(nums[2]))
    else:
        root = nums[root_idx]
        root = TreeNode(root)
        root.left = sorted_array_to_bst(nums[:root_idx])
        root.right = sorted_array_to_bst(nums[root_idx+1:])
        return root


print(sorted_array_to_bst([3, 5, 8]))

