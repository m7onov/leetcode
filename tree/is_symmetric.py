"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/627/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

Follow up: Solve it both recursively and iteratively.
"""
from itertools import zip_longest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


def inorder_tree_walk(root: TreeNode, from_left_to_right: bool = True):
    if root is None:
        return

    branch_primary = 'left' if from_left_to_right else 'right'
    branch_secondary = 'right' if from_left_to_right else 'left'
    stack_direction = 'down'
    stack = [(root, None)]
    while len(stack) > 0:
        if stack_direction == 'down':
            cur_node = getattr(stack[-1][0], branch_primary)
            if cur_node is not None:
                stack.append((cur_node, branch_primary))
                continue

            stack_direction = 'up'

        elif stack_direction == 'up':
            cur_node, node_branch = stack.pop()
            yield cur_node, node_branch
            cur_node = getattr(cur_node, branch_secondary)
            if cur_node is not None:
                stack.append((cur_node, branch_secondary))
                stack_direction = 'down'

        else:
            raise Exception('unexpected dir')


def postorder_tree_walk(root: TreeNode, from_left_to_right: bool = True):
    if root is None:
        return

    branch_primary = 'left' if from_left_to_right else 'right'
    branch_secondary = 'right' if from_left_to_right else 'left'
    stack_direction = 'down'
    stack = [(root, None)]
    while len(stack) > 0:
        if stack_direction == 'down':
            cur_node = getattr(stack[-1][0], branch_primary)
            if cur_node is not None:
                stack.append((cur_node, branch_primary))
                continue

            cur_node = getattr(stack[-1][0], branch_secondary)
            if cur_node is not None:
                stack.append((cur_node, branch_secondary))
                continue

            stack_direction = 'up'

        elif stack_direction == 'up':
            cur_node, node_branch = stack.pop()
            yield cur_node, node_branch
            if node_branch == branch_primary:
                cur_node = getattr(stack[-1][0], branch_secondary)
                if cur_node is not None:
                    stack.append((cur_node, branch_secondary))
                    stack_direction = 'down'

        else:
            raise Exception('unexpected dir')


def preorder_tree_walk(root: TreeNode, from_left_to_right: bool = True):
    if root is None:
        return

    branch_primary = 'left' if from_left_to_right else 'right'
    branch_secondary = 'right' if from_left_to_right else 'left'
    stack = [(root, None)]
    while len(stack) > 0:
        cur_node, node_branch = stack.pop()
        yield cur_node, node_branch

        node = getattr(cur_node, branch_secondary)
        if node is not None:
            stack.append((node, branch_secondary))

        node = getattr(cur_node, branch_primary)
        if node is not None:
            stack.append((node, branch_primary))


def is_symmetric_bottom_to_top(root: TreeNode, variant: str = 'inorder'):
    if variant == 'inorder':
        walker = zip(inorder_tree_walk(root), inorder_tree_walk(root, False))

    elif variant == 'postorder':
        walker = zip(postorder_tree_walk(root), postorder_tree_walk(root, False))

    else:
        raise Exception('unknown variant: ', variant)

    for p, s in walker:
        if p[1] is None or s[1] is None:
            if p[1] is not None or s[1] is not None:
                return False

            return True

        if p[0].val != s[0].val or p[1] == s[1]:
            return False


def is_symmetric_top_to_bottom(root: TreeNode):
    walker = zip_longest(preorder_tree_walk(root.left),
                         preorder_tree_walk(root.right, False))

    for p, s in walker:
        if p is None or s is None:
            return False

        if p[1] is None or s[1] is None:
            if p[1] is not None or s[1] is not None:
                return False
            elif p[0].val != s[0].val:
                return False

            continue

        if p[0].val != s[0].val or p[1] == s[1]:
            return False

    return True


def is_symmetric(root: TreeNode) -> bool:
    if root is None:
        return True

    return is_symmetric_bottom_to_top(root, 'inorder')
    # return self.is_symmetric_bottom_to_top(root, 'postorder')
    # return self.is_symmetric_top_to_bottom(root)
