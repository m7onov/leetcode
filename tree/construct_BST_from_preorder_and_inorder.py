"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/788/

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is
the inorder traversal of the same tree, construct and return the binary tree.

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""
from typing import List, Optional
from tree import TreeNode

"""
In the tree/construct_BST_from_preorder.py conditions are relaxed. There should be possible to construct multiple
trees from inorder array, e.g.:
    inorder array: [3,2,1]
    variant1:
                   1
                  /
                 2
                /
               3
    variant2:
                    2
                  /   \
                 3     1
In this task we have preorder array which narrows down possible solutions
"""
def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # когда в inorder встретим элемент == preorder[0] это будет означать границу левого поддерева
    root = None
    cur_node = None
    cur_chain = None
    for i, v in enumerate(preorder):
        print(f'preorder next: {v}')

        if cur_chain is None:
            cur_chain = TreeNode(v)
            print(f'initialize cur_chain: {v}')

        # нашли самый левый узел
        if v == inorder[0]:
            a = TreeNode(v)
            a.left = cur_chain
            root = cur_chain
            print(f'found leftmost node: {v}')
            break
        else:
            if cur_node is not None:
                print(f'append {v} to {cur_node.val}.left')
                cur_node.left = TreeNode(v)
                cur_node = cur_node.left
            else:
                print(f'initialize cur_node: {v}')
                cur_node = TreeNode(v)


    return root

"""

       3
      /  \
     9    20
         /  \
       15    7

"""

tr = TreeNode(3)
tr.left = TreeNode(9)
tr.right = TreeNode(20)
tr.right.left = TreeNode(15)
tr.right.right = TreeNode(7)

print(build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))

