"""
This is my own implementation of binary tree

https://en.wikipedia.org/wiki/Binary_tree
"""
from typing import Optional, Iterator


class TreeNode:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class BinaryTree:

    def __init__(self, root: TreeNode = None):
        self.root = root
        if self.root is None:
            self.root = TreeNode()

    @staticmethod
    def check_path(path: str, is_raise: bool = True):
        if path == '':
            if is_raise:
                raise Exception(f'empty tree path: {path}')
            else:
                return False

        for c in path:
            if c not in ('l', 'r'):
                if is_raise:
                    raise Exception(f'invalid binary tree path: {path}')
                else:
                    return False

        return True

    @staticmethod
    def validate_path(path: str, is_raise: bool = True) -> str:
        path = path.strip().lower()
        BinaryTree.check_path(path, is_raise)
        return path

    @staticmethod
    def get_child(node: TreeNode, direction: str) -> TreeNode:
        if direction == 'l':
            return node.left
        elif direction == 'r':
            return node.right
        else:
            raise Exception('unexpected')

    @staticmethod
    def put_child(node: TreeNode, direction: str, child: TreeNode) -> TreeNode:
        if direction == 'l':
            node.left = child
        elif direction == 'r':
            node.right = child
        else:
            raise Exception('unexpected')

        return child

    def get_node(self, path: str) -> Optional[TreeNode]:
        """
        :param path: node path in current tree, e.g. 'lrrlrr', case insensitive, non-empty
        :return: requested node or None
        """
        path = BinaryTree.validate_path(path)
        node = self.root
        for d in path:
            if node is not None:
                if d == 'l':
                    node = node.left
                elif d == 'r':
                    node = node.right
                else:
                    raise Exception('unexpected')
            else:
                return None

    def put_node(self, path: str, node: TreeNode):
        """
        :param path: node path in current tree, e.g. 'lrrlrr', case insensitive, non-empty
        :param node: target node to be put
        :return:
        """
        path = BinaryTree.validate_path(path)
        cur_node = self.root
        for d in path[:-1]:
            next_node = BinaryTree.get_child(cur_node, d)
            if next_node is None:
                next_node = BinaryTree.put_child(cur_node, d, TreeNode())

            cur_node = next_node

        BinaryTree.put_child(cur_node, path[-1], node)

    @staticmethod
    def inorder_tree_walk_recursion(root: TreeNode) -> Iterator[TreeNode]:
        if root is None:
            return

        yield from BinaryTree.inorder_tree_walk_recursion(root.left)
        yield root
        yield from BinaryTree.inorder_tree_walk_recursion(root.right)

    def inorder_tree_walk(self) -> Iterator[TreeNode]:
        yield from self.inorder_tree_walk_recursion(self.root)

    def preorder_tree_walk(self) -> Iterator[TreeNode]:
        pass

    def postorder_tree_walk(self) -> Iterator[TreeNode]:
        pass


# bst = BinaryTree()
# bst.put_node('lrlrlrl', TreeNode('hello'))
# print(bst)

_root = TreeNode(7)
_root.left = TreeNode(3)
_root.right = TreeNode(15)
_root.right.left = TreeNode(9)
_root.right.right = TreeNode(20)

_tree = BinaryTree(_root)
for _node in _tree.inorder_tree_walk():
    print(_node)
