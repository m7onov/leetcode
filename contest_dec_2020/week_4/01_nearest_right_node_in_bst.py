"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3576/

Given the root of a binary tree and a node u in the tree, return the nearest node on the same level that is to the right
of u, or return null if u is the rightmost node in its level.

Example 1:
Input: root = [1,2,3,null,4,5,6], u = 4
Output: 5
Explanation: The nearest node on the same level to the right of node 4 is node 5.

Example 2:
Input: root = [3,null,4,2], u = 2
Output: null
Explanation: There are no nodes to the right of 2.

Example 3:
Input: root = [1], u = 1
Output: null

Example 4:
Input: root = [3,4,2,null,null,null,1], u = 4
Output: 2

Constraints:
The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 10^5
All values in the tree are distinct.
u is a node in the binary tree rooted at root.
"""
from typing import Optional, List

from tree import TreeNode, init_tree_from_level_array


def find_nearest_right_node_bfs(root: TreeNode, val: int) -> Optional[TreeNode]:

    def bfs(prev_level: List[TreeNode]) -> Optional[TreeNode]:
        if len(prev_level) == 0:
            return None

        found = False
        next_node = None
        next_level = []
        for n in prev_level:
            if not found and n.val == val:
                found = True
            elif found and n.val is not None:
                next_node = n
                break

            if n.left is not None:
                next_level.append(n.left)
            if n.right is not None:
                next_level.append(n.right)

        if next_node is not None:
            return next_node
        else:
            return bfs(next_level)

    return bfs([root])


def find_nearest_right_node_dfs(root: TreeNode, val: int) -> Optional[TreeNode]:

    def dfs(node: TreeNode, depth: int) -> Optional[TreeNode]:
        nonlocal val_node, val_depth

        if val_node is None and node.val == val:
            val_node = node
            val_depth = depth

        elif val_node is not None and node.val is not None and depth == val_depth:
            return node

        if node.left is not None:
            next_node = dfs(node.left, depth+1)
            if next_node is not None:
                return next_node

        if node.right is not None:
            next_node = dfs(node.right, depth+1)
            if next_node is not None:
                return next_node

        return None

    val_node = None
    val_depth = -1
    return dfs(root, 0)


_root = init_tree_from_level_array([8, 38, 29, 7, 39, 13, 12, 18, 30, 1, 16, None, 26, 10, 5, None, 24, None, 17, 36,
                                    9, None, 34, 27, None, None, None, 33, 19, None, 25, None, None, None, None, None,
                                    None, 32, None, 3, 22, None, None, None, 40, None, None, 14, None, 20, None, None,
                                    None, 37, 21, 11, 15, None, None, None, 28, 31, 23, None, None, None, None, None,
                                    None, 6, 4, None, 2, None, None, None, None, None, 35])

# print(find_nearest_right_node_bfs(_root, 20))
print(find_nearest_right_node_dfs(_root, 20))
