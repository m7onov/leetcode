"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/790/

Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

Example 1:

.. image:: https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 10^4
0 <= Node.val <= 10^4

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth
smallest frequently, how would you optimize?
"""
from typing import Optional
from tree import TreeNode


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    kth_idx = 0

    def visit_inorder(node: TreeNode):
        nonlocal kth_idx

        if node is None:
            return None

        ret = visit_inorder(node.left)
        if ret is not None:
            return ret

        kth_idx += 1
        if kth_idx == k:
            return node.val

        return visit_inorder(node.right)

    return visit_inorder(root)


tr = TreeNode(3)
tr.left = TreeNode(1)
tr.right = TreeNode(1)
tr.left.right = TreeNode(2)

res = kth_smallest(tr, 1)
print(res)

tr = TreeNode(5)
tr.left = TreeNode(3)
tr.right = TreeNode(6)
tr.left.left = TreeNode(2)
tr.left.right = TreeNode(4)
tr.left.left.left = TreeNode(1)

res = kth_smallest(tr, 3)
print(res)
