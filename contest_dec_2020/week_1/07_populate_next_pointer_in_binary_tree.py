"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3556/

Given a binary tree
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be
set to NULL.
Initially, all next pointers are set to NULL.

Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its
next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with
'#' signifying the end of each level.

Constraints:
The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
"""
from typing import Optional
from tree import TreeNodeLL


def get_next_level_leftmost_node(node: TreeNodeLL) -> Optional[TreeNodeLL]:
    if node.left is not None:
        node = node.left
    elif node.right is not None:
        node = node.right
    elif node.next is not None:
        node = get_next_level_leftmost_node(node.next)
    else:
        node = None

    return node


def connect_trees(left_tree: TreeNodeLL, right_tree: TreeNodeLL):
    left_tree_left_edge = left_tree
    right_tree_left_edge = right_tree

    while left_tree_left_edge is not None and right_tree_left_edge is not None:
        left_tree_right_edge = left_tree_left_edge
        while left_tree_right_edge.next is not None:
            left_tree_right_edge = left_tree_right_edge.next

        left_tree_left_edge = get_next_level_leftmost_node(left_tree_left_edge)

        print(f'{left_tree_right_edge} --> {right_tree_left_edge}')
        left_tree_right_edge.next = right_tree_left_edge

        right_tree_left_edge = get_next_level_leftmost_node(right_tree_left_edge)


def connect(root: TreeNodeLL) -> Optional[TreeNodeLL]:
    if root is None:
        return root

    connect(root.left)
    connect(root.right)

    if root.left is not None and root.right is not None:
        connect_trees(root.left, root.right)

    return root


# _root = TreeNodeLL(0)
# _root.left = TreeNodeLL(1)
# _root.right = TreeNodeLL(2)
# _root.left.left = TreeNodeLL(3)
# _root.left.right = TreeNodeLL(4)
# _root.right.left = TreeNodeLL(5)
# _root.right.right = TreeNodeLL(6)
# _root.left.left.left = TreeNodeLL(7)
# _root.left.left.right = TreeNodeLL(8)
# _root.left.right.left = TreeNodeLL(9)
# _root.left.right.right = TreeNodeLL(10)

# _root = TreeNodeLL(1)
# _root.left = TreeNodeLL(2)
# _root.right = TreeNodeLL(3)
# _root.left.left = TreeNodeLL(4)
# _root.right.right = TreeNodeLL(5)

# _root = TreeNodeLL(1)
# _root.left = TreeNodeLL(2)
# _root.right = TreeNodeLL(3)
# _root.left.left = TreeNodeLL(4)
# _root.left.right = TreeNodeLL(5)
# _root.right.right = TreeNodeLL(6)
# _root.left.left.left = TreeNodeLL(7)
# _root.right.right.right = TreeNodeLL(8)

_root = TreeNodeLL(2)
_root.left = TreeNodeLL(1)
_root.right = TreeNodeLL(3)
_root.left.left = TreeNodeLL(0)
_root.left.right = TreeNodeLL(7)
_root.right.left = TreeNodeLL(9)
_root.right.right = TreeNodeLL(1)
_root.left.left.left = TreeNodeLL(2)
_root.left.right.left = TreeNodeLL(1)
_root.left.right.right = TreeNodeLL(0)
_root.right.right.left = TreeNodeLL(8)
_root.right.right.right = TreeNodeLL(8)
_root.left.right.right.left = TreeNodeLL(7)

connect(_root)
