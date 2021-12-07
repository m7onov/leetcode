"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or
another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a
string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily
need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:

.. image: https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [1,2]

Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-1000 <= Node.val <= 1000
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root) -> str:
        ret_str = []

        def serialize_subtree(root):
            nonlocal ret_str
            if root is None:
                return
            if root.left is not None:
                ret_str.append('l')
                serialize_subtree(root.left)
            ret_str.append(str(root.val))
            if root.right is not None:
                ret_str.append('r')
                serialize_subtree(root.right)
            ret_str.append('u')

        serialize_subtree(root)
        return '|'.join(ret_str)

    def deserialize(self, data) -> TreeNode:
        root = None
        path = []
        for i in [x for x in data.split('|') if len(x) > 0]:
            if root is None:
                root = TreeNode(None)
                path.append(root)
            node = path[-1]
            if i == 'l':
                node.left = TreeNode(None)
                node = node.left
                path.append(node)
            elif i == 'r':
                node.right = TreeNode(None)
                node = node.right
                path.append(node)
            elif i == 'u':
                path.pop()
            else:
                node.val = i
        return root


def tests():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.right.left = TreeNode(4)
    tree.right.right = TreeNode(5)
    tree.right.right.left = TreeNode(6)
    codec = Codec()
    res = codec.serialize(tree)
    print(f'serialized = {res}')
    tree = codec.deserialize(res)
    res = codec.serialize(tree)
    print(f'  original = {res}')
    #
    tree = TreeNode(2)
    tree.right = TreeNode(1)
    tree.right.right = TreeNode(3)
    tree.right.right.left = TreeNode(4)
    tree.right.right.right = TreeNode(5)
    tree.right.right.right.left = TreeNode(6)
    codec = Codec()
    res = codec.serialize(tree)
    print(f'serialized = {res}')
    tree = codec.deserialize(res)
    res = codec.serialize(tree)
    print(f'  original = {res}')
    #
    tree = TreeNode(2)
    codec = Codec()
    res = codec.serialize(tree)
    print(f'serialized = {res}')
    tree = codec.deserialize(res)
    res = codec.serialize(tree)
    print(f'  original = {res}')
    tree = None
    codec = Codec()
    res = codec.serialize(tree)
    print(f'serialized = {res}')
    tree = codec.deserialize(res)
    res = codec.serialize(tree)
    print(f'  original = {res}')
    #
    tree = TreeNode(-2)
    tree.right = TreeNode(-1)
    tree.right.right = TreeNode(-3)
    tree.right.right.left = TreeNode(-4)
    tree.right.right.right = TreeNode(-5)
    tree.right.right.right.left = TreeNode(-6)
    codec = Codec()
    res = codec.serialize(tree)
    print(f'serialized = {res}')
    tree = codec.deserialize(res)
    res = codec.serialize(tree)
    print(f'  original = {res}')


tests()






