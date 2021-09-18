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
NOTE:
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

"""
NOTE:
Свойства inorder порядка для поддерева с корнем root:
    1) первый элемент - это крайний левый элемент в поддереве
    2) последний элемент - это root
    3) следующий за крайним левым элементом - самый нижний элемент, имеющий правое поддерево

Свойства preorder порядка для поддерева с корнем root:
    1) левая грань дерева начинается с элемента root и заканчивается элементом с left == None
    2) левая грань дерева заканчивает крайним левым элементом в поддереве
"""


def build_tree_non_recursive(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    preorder_nodes = {}
    preorder_chain_start = None
    preorder_prev_node = None
    inorder_next_idx = 0
    inorder_next_val = inorder[inorder_next_idx]
    inorder_prev_val = None

    # walking through preorder list
    for preorder_next_val in preorder:
        preorder_next_node = TreeNode(preorder_next_val)
        preorder_nodes[preorder_next_val] = preorder_next_node

        # start new chain
        if preorder_chain_start is None:
            preorder_chain_start = preorder_next_node
            # we need to connect new chain to a specific node in previous chain
            if inorder_prev_val is not None:
                preorder_nodes[inorder_prev_val].right = preorder_next_node
                inorder_prev_val = None
        # or add to existing chain's tail
        else:
            if preorder_prev_node is not None:
                preorder_prev_node.left = preorder_next_node

        # we found chain end
        if inorder_next_val in preorder_nodes:
            # forward to next element in inorder list which was not seen in preorder list
            while inorder_next_val in preorder_nodes:
                inorder_prev_val = inorder_next_val
                inorder_next_idx += 1
                if inorder_next_idx < len(inorder):
                    inorder_next_val = inorder[inorder_next_idx]
                else:
                    inorder_next_val = None

            # reset chain
            preorder_chain_start = None
            preorder_prev_node = None
        else:
            preorder_prev_node = preorder_next_node

    return preorder_nodes[preorder[0]]


def build_tree_recursive(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    preorder_idx = -1

    def split(inorder_start: int, inorder_end: int):
        if inorder_start == inorder_end:
            return None

        nonlocal preorder_idx
        preorder_idx += 1

        for i in range(inorder_start, inorder_end):
            if inorder[i] == preorder[preorder_idx]:
                ret = TreeNode(preorder[preorder_idx])
                ret.left = split(inorder_start, i)
                ret.right = split(i + 1, inorder_end)
                return ret

        raise Exception('unexpected state')

    return split(0, len(inorder))


# print(build_tree_recursive([3, 9, 20, 15, 7],
#                            [9, 3, 15, 20, 7]).to_full_str())

# print(build_tree_recursive([1, 2, 3, 4, 6, 5, 7, 8, 9, 10, 11],
#                            [4, 5, 6, 7, 3, 10, 9, 11, 8, 2, 1]).to_full_str())


print(build_tree_recursive([7, 6, 8, 1, 2, 3, 4, 5],
                           [6, 1, 8, 2, 7, 4, 3, 5]).to_full_str())
