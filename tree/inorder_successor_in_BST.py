"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/791/

Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST.
If the given node has no in-order successor in the tree, return null.
The successor of a node p is the node with the smallest key greater than p.val.

Example 1:

.. image:: https://assets.leetcode.com/uploads/2019/01/23/285_example_1.PNG

Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

Example 2:

.. image:: https://assets.leetcode.com/uploads/2019/01/23/285_example_2.PNG

Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.


Constraints:
    | The number of nodes in the tree is in the range [1, 10^4].
    | -10^5 <= Node.val <= 10^5
    | All Nodes will have unique values.
"""
from typing import Optional
from tree import TreeNode


def inorder_successor(root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    node = root
    path = []
    while node is not None:
        print(f'path = {path}')
        if p.val != node.val:
            path.append(node)
            if p.val < node.val:
                print('going down to the left')
                node = node.left
            elif p.val > node.val:
                print('going down to the right')
                node = node.right
        else:
            print('found then node')
            print(f'searching for the leftmost node in right subtree of {node}')
            ret_node = node.right
            while ret_node is not None and ret_node.left is not None:
                ret_node = ret_node.left
                print(f'ret_node = {ret_node}')

            print(f'ret_node = {ret_node}')
            if ret_node is None:
                print(f'did not find; returning ancestor')
                for i in range(len(path)-1, -1, -1):
                    if path[i].left == node:
                        ret_node = path[i]
                        break
                    else:
                        node = path[i]

            return ret_node


# O(1) memory
def inorder_successor2(root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    node = root
    last_left_branch = None
    while node is not None:
        if p.val != node.val:
            if p.val < node.val:
                print('going down to the left')
                last_left_branch = node
                node = node.left
            elif p.val > node.val:
                print('going down to the right')
                node = node.right
        else:
            print('found then node')
            print(f'searching for the leftmost node in right subtree of {node}')
            ret_node = node.right
            while ret_node is not None and ret_node.left is not None:
                ret_node = ret_node.left
                print(f'ret_node = {ret_node}')

            print(f'ret_node = {ret_node}')
            if ret_node is None:
                print(f'did not find; returning last left branch')
                ret_node = last_left_branch

            return ret_node


tr = TreeNode(2)
tr.left = TreeNode(1)
tr.right = TreeNode(3)

res = inorder_successor2(tr, tr.left)
print(f'2 == {res}')

print('------------------')

tr = TreeNode(5)
tr.left = TreeNode(3)
tr.right = TreeNode(6)
tr.left.left = TreeNode(2)
tr.left.right = TreeNode(4)
tr.left.left.left = TreeNode(1)

res = inorder_successor2(tr, tr.right)
print(f'None == {res}')

print('------------------')

tr = TreeNode(0)
res = inorder_successor(tr, tr)
print(f'None == {res}')

print('------------------')

tr = TreeNode(2)
tr.right = TreeNode(3)
res = inorder_successor2(tr, tr)
print(f'3 == {res}')

print('------------------')

tr = TreeNode(6)
tr.left = TreeNode(2)
tr.right = TreeNode(8)
tr.left.left = TreeNode(0)
tr.left.right = TreeNode(4)
tr.right.left = TreeNode(7)
tr.right.right = TreeNode(9)
tr.left.right.left = TreeNode(3)
tr.left.right.right = TreeNode(5)

res = inorder_successor2(tr, tr.left)
print(f'3 == {res}')

print('------------------')

tr = TreeNode(5)
tr.left = TreeNode(3)
tr.right = TreeNode(6)
tr.left.left = TreeNode(2)
tr.left.right = TreeNode(4)
tr.left.right.left = TreeNode(1)

res = inorder_successor2(tr, tr.right)
print(f'None == {res}')
