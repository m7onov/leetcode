"""
This is my own implementation of binary tree

https://en.wikipedia.org/wiki/Binary_tree
"""
from typing import Optional


class TreeNode:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:

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
        BST.check_path(path, is_raise)
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
        path = BST.validate_path(path)
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
        path = BST.validate_path(path)
        cur_node = self.root
        for d in path[:-1]:
            next_node = BST.get_child(cur_node, d)
            if next_node is None:
                next_node = BST.put_child(cur_node, d, TreeNode())

            cur_node = next_node

        BST.put_child(cur_node, path[-1], node)

    def inorder_tree_walk(self):
        pass


bst = BST()
bst.put_node('lrlrlrl', TreeNode('hello'))
print(bst)
