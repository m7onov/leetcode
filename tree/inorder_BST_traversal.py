"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/786/

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

.. image:: https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:

.. image:: https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg

Input: root = [1,2]
Output: [2,1]

Example 5:

.. image:: https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg

Input: root = [1,null,2]
Output: [1,2]


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import Optional, List
from tree import TreeNode, init_tree_from_level_array


class Solution:
    # O(n) memory
    # O(n) speed
    def inorder_traversal_first_solution(self, root: Optional[TreeNode]) -> List[int]:
        # Note: look at contest_dec_2020/week2/03_bst_inorder_iterator.py
        if root is None:
            return []

        traverse_path = []
        stack = [root]
        stack_dir = 'down'
        while len(stack) > 0:
            stack_head = stack[-1]
            print('stack:', stack, 'dir: ', stack_dir)

            if stack_head.left is not None and stack_dir == 'down':
                stack.append(stack_head.left)
                continue

            traverse_path.append(stack_head.val)
            stack.pop()

            if stack_head.right is not None:
                stack.append(stack_head.right)
                stack_dir = 'down'
                continue

            stack_dir = 'up'

        return traverse_path

    # O(n) memory
    # O(n) speed
    def inorder_traversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(node: TreeNode):
            if node is not None:
                if node.left is not None:
                    helper(node.left)
                res.append(node.val)
                if node.right is not None:
                    helper(node.right)

        helper(root)
        return res

    # O(n) memory
    # O(n) speed
    def inorder_traversal_second_solution(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur_node = root
        right_dir = False

        while cur_node is not None:
            while cur_node.left is not None and not right_dir:
                stack.append(cur_node)
                cur_node = cur_node.left

            res.append(cur_node.val)

            if cur_node.right is not None:
                cur_node = cur_node.right
                right_dir = False
            else:
                cur_node = stack.pop() if len(stack) > 0 else None
                right_dir = True

        return res

    # O(n) memory
    # O(n) speed
    def inorder_traversal_third_solution(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur_node = root

        while cur_node is not None or len(stack) > 0:
            while cur_node is not None:
                stack.append(cur_node)
                cur_node = cur_node.left

            cur_node = stack.pop()
            res.append(cur_node.val)
            cur_node = cur_node.right

        return res

    # O(1) memory
    # O(n) speed
    def inorder_traversal_o1_solution(self, root: Optional[TreeNode]) -> List[int]:
        pass


sol = Solution()

# tr = TreeNode(1)
# tr.right = TreeNode(2)
# tr.right.left = TreeNode(3)
# print(sol.inorderTraversal(tr))

# tr = TreeNode(1)
# tr.left = TreeNode(2)
# tr.right = TreeNode(3)
# tr.right.left = TreeNode(4)
# tr.right.right = TreeNode(5)
# print(sol.inorderTraversal(tr))

tr = TreeNode(1)
tr.left = TreeNode(2)
tr.right = TreeNode(3)
tr.right.left = TreeNode(4)
tr.right.right = TreeNode(5)
print(sol.inorderTraversal2(tr))
