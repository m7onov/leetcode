"""
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has
a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal
displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given
requirements.

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Constraints:
1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.
"""
from typing import List
from tree import TreeNode


def bst_from_preorder(preorder: List[int]) -> TreeNode:
    root = TreeNode(preorder[0])
    stack = [root]
    for v in preorder[1:]:
        if v < stack[-1].val:
            node = TreeNode(v)
            stack[-1].left = node
            stack.append(node)

        else:
            node = stack[-1]
            while len(stack) > 0 and v > stack[-1].val:
                node = stack.pop()

            node.right = TreeNode(v)
            stack.append(node.right)

    return root


# print(bst_from_preorder([16, 8, 4, 2, 6, 12, 10, 14, 24, 20, 28, 26, 30]))
print(bst_from_preorder([8, 5, 1, 7, 10, 12]))

