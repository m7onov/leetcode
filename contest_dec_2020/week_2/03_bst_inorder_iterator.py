"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3560/

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

- BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the
  constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.

- boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns
  false.

- int next() Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the
smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order
traversal when next() is called.

Example 1:
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False

Constraints:
The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next.

Follow up:
Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?
"""
from typing import Optional, Tuple, List, Iterator


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class BstIteratorNonRecursive:

    def __init__(self, root: TreeNode):
        self.stack_direction = 'down'
        self.stack: List[TreeNode] = [root]

    def __next__(self) -> Optional[int]:
        if len(self.stack) == 0:
            return None

        while len(self.stack) > 0:
            if self.stack_direction == 'down':
                cur_node = self.stack[-1].left
                if cur_node is not None:
                    self.stack.append(cur_node)
                else:
                    self.stack_direction = 'up'

            else:
                ret_node = self.stack.pop()

                cur_node = ret_node.right
                if cur_node is not None:
                    self.stack.append(cur_node)
                    self.stack_direction = 'down'

                return ret_node.val

    def has_next(self) -> bool:
        return len(self.stack) > 0


class BstIteratorRecursive:

    @staticmethod
    def inorder_tree_walk_recursion(root: TreeNode) -> Iterator[TreeNode]:
        if root is None:
            return
        yield from BstIteratorRecursive.inorder_tree_walk_recursion(root.left)
        yield root
        yield from BstIteratorRecursive.inorder_tree_walk_recursion(root.right)

    def __init__(self, root: TreeNode):
        self.it = BstIteratorRecursive.inorder_tree_walk_recursion(root)
        self.ret_node = None

    def __next__(self):
        node = self.ret_node
        if node is None:
            node = self.it.__next__()
        return node

    def has_next(self):
        try:
            self.ret_node = self.it.__next__()
            return True
        except StopIteration:
            return False


_root = TreeNode(7)
_root.left = TreeNode(3)
_root.right = TreeNode(15)
_root.right.left = TreeNode(9)
_root.right.right = TreeNode(20)

it = BstIteratorNonRecursive(_root)
# it = BstIteratorRecursive(_root)

print(it.__next__())
print(it.__next__())
print(it.has_next())
print(it.__next__())
print(it.has_next())
print(it.__next__())
print(it.has_next())
print(it.__next__())
print(it.has_next())
