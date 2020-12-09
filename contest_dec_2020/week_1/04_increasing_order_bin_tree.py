"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3553/

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the
root of the tree, and every node has no left child and only one right child.

Example 1:
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:
Input: root = [5,1,7]
Output: [1,null,5,null,7]
"""
from typing import List


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def inorder_tree_walk(root: TreeNode, head_and_tail: List):
    if root is None:
        return

    # left subtree
    inorder_tree_walk(root.left, head_and_tail)

    if head_and_tail[0] is None:
        head_and_tail[0] = root

    if head_and_tail[1] is not None:
        head_and_tail[1].left = None
        head_and_tail[1].right = root

    head_and_tail[1] = root

    # right subtree
    inorder_tree_walk(root.right, head_and_tail)

    head_and_tail[1].left = None
    head_and_tail[1].right = None

    return head_and_tail


def increasing_bst(root: TreeNode):
    head_and_tail = inorder_tree_walk(root, [None, None])
    return head_and_tail[0]


def increasing_bst_nice(root: TreeNode):
    def inorder(node):
        if node:
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right

        return ans.right


# root = TreeNode(5)
# root.left = TreeNode(3)
# root.left.left = TreeNode(2)
# root.left.left.left = TreeNode(1)
# root.left.right = TreeNode(4)
# root.right = TreeNode(6)
# root.right.right = TreeNode(8)
# root.right.right.left = TreeNode(7)
# root.right.right.right = TreeNode(9)


_root = TreeNode(2)
_root.left = TreeNode(1)
_root.right = TreeNode(4)
_root.right.left = TreeNode(3)

print(increasing_bst(_root))
