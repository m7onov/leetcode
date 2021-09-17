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
def build_tree1(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    head = None
    tail = None

    def move_tail(d, v):
        nonlocal tail, head
        if tail is None:
            head = TreeNode(v)
            tail = head
        elif d == 'l':
            tail.left = TreeNode(v)
            tail = tail.left
        elif d == 'r':
            tail.right = TreeNode(v)
            tail = tail.right

    preorder_seen = set()
    inorder_idx = 0
    fork = False
    for v in preorder:
        print(f'next preorder: {v}, head = {head}, tail = {tail}')
        if v == inorder[inorder_idx]:
            print(f'match inorder next {v}')
            if v in preorder_seen:
                print(f'seen this element if preorder chain, passing')
                continue
            else:
                if fork:
                    print(f'moving tail {tail} to the right {v}')
                    move_tail('r', v)
                else:
                    print(f'moving tail {tail} to the left {v}')
                    move_tail('l', v)
                    fork = True

            inorder_idx += 1
        else:
            if fork:
                print(f'moving tail {tail} to the right {v}')
                move_tail('r', v)
            else:
                print(f'moving tail {tail} to the left {v}')
                move_tail('l', v)


def build_tree2(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    nodes = dict()
    prev_node = None
    inorder_idx = 0
    move_right = False
    for v in preorder:
        node = TreeNode(v)
        nodes[v] = node
        if v == inorder[inorder_idx]:
            print(f'break on {v}')
            print(f'nodes = {nodes}')
            while inorder[inorder_idx] in nodes:
                prev_node = nodes[inorder[inorder_idx]]
                inorder_idx += 1
            print(f'prev_node = {prev_node}')
            print(f'inorder next = {inorder[inorder_idx]}')
            # break
        else:
            if prev_node is not None:
                if move_right:
                    prev_node.right = node
                    move_right = False
                else:
                    prev_node.left = node

            prev_node = node


"""

       3
      /  \
     9    20
         /  \
       15    7

inorder:  9 3 15 20 7
preorder: 3 9 20 15 7

"""

tr = TreeNode(3)
tr.left = TreeNode(9)
tr.right = TreeNode(20)
tr.right.left = TreeNode(15)
tr.right.right = TreeNode(7)

# print(build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
print(build_tree2([1, 2, 3, 4, 6, 5, 7, 8, 9, 10, 11],
                  [4, 5, 6, 7, 3, 10, 9, 11, 8, 2, 1]))


"""

Свойства inorder порядка для поддерева с корнем root:
    1) первый элемент - это крайний левый элемент в поддереве
    2) последний элемент - это root
    3) следующий за крайним левым элементом - самый нижний элемент, имеющий правое поддерево

Свойства preorder порядка для поддерева с корнем root:
    1) левая грань дерева начинается с элемента root и заканчивается элементом с left == None
    2) левая грань дерева заканчивает крайним левым элементом в поддереве



"""

