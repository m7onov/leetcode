"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/625/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:
    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def is_valid_bst_iterative(root: TreeNode) -> bool:
    if root is None:
        return True

    stack = [(root, None, None)]

    while len(stack) > 0:
        cur_node, min_val, max_val = stack.pop()
        if min_val is not None:
            if cur_node.val <= min_val:
                return False

        if max_val is not None:
            if cur_node.val >= max_val:
                return False

        if cur_node.right is not None:
            stack.append((cur_node.right, cur_node.val, max_val))

        if cur_node.left is not None:
            stack.append((cur_node.left, min_val, cur_node.val))

    return True


def is_valid_bst_recursive(root: TreeNode, min_val: int = None, max_val: int = None) -> bool:
    if root is None:
        return True

    is_left_valid = is_valid_bst_recursive(root.left, min_val, root.val)
    is_right_valid = is_valid_bst_recursive(root.right, root.val, max_val)

    if not is_left_valid or \
            not is_right_valid or \
            min_val is not None and root.val <= min_val or \
            max_val is not None and root.val >= max_val:
        return False

    return True


def is_valid_bst(self, root: TreeNode) -> bool:
    return self.is_valid_bst_recursive(root)
    # return self.is_valid_bst_iterative(root)
