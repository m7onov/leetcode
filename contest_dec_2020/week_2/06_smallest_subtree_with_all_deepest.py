"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3563/

Given the root of a binary tree, the depth of each node is the shortest distance to the root.
Return the smallest subtree such that it contains all the deepest nodes in the original tree.
A node is called the deepest if it has the largest depth possible among any node in the entire tree.
The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.
Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we
return it.

Example 2:
Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.

Example 3:
Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree
of node 2 is the smallest.

Constraints:
The number of nodes in the tree will be in the range [1, 500].
0 <= Node.val <= 500
The values of the nodes in the tree are unique.
"""
from typing import List
from tree import TreeNode


def dfs(root: TreeNode, upper_path: List[TreeNode], deepest_paths: List[List[TreeNode]]):
    if root is None:
        return

    if root.left is None and root.right is None:
        if len(deepest_paths) == 0 or len(deepest_paths[0]) < len(upper_path) + 1:
            deepest_paths.clear()
            deepest_paths.append(upper_path + [root])

        elif len(deepest_paths[0]) == len(upper_path) + 1:
            deepest_paths.append(upper_path + [root])

        return

    dfs(root.left, upper_path + [root], deepest_paths)
    dfs(root.right, upper_path + [root], deepest_paths)


def subtree_with_all_deepest(root: TreeNode) -> TreeNode:
    deepest_paths = []
    dfs(root, [], deepest_paths)
    if len(deepest_paths) == 1:
        return deepest_paths[0][-1]

    for i in range(len(deepest_paths[0])):
        val = deepest_paths[0][i]
        for path in deepest_paths[1:]:
            if path[i] != val:
                return path[i-1]

    return deepest_paths[0][0]


_root = TreeNode(3)
_root.left = TreeNode(5)
_root.right = TreeNode(1)
_root.left.left = TreeNode(6)
_root.left.right = TreeNode(2)
_root.right.left = TreeNode(0)
_root.right.right = TreeNode(8)
_root.left.right.left = TreeNode(7)
_root.left.right.right = TreeNode(4)

# _root = TreeNode(1)

# _root = TreeNode(0)
# _root.left = TreeNode(1)
# _root.right = TreeNode(3)
# _root.left.right = TreeNode(2)

print(subtree_with_all_deepest(_root))
