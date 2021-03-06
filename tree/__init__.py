from typing import List

import binarytree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()


class TreeNodeLL:
    def __init__(self, val=0, left=None, right=None, nx=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = nx

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()


def init_tree_from_level_array(array: List[int]) -> TreeNode:
    root = TreeNode(array[0])
    prev_level = [root]
    level_num = 1
    level_start_idx = 1
    while (level_start_idx + 2 ** level_num) <= len(array):
        level = []
        for i in range(2 ** level_num):
            node = TreeNode(array[level_start_idx + i])
            level.append(node)
            if i % 2 == 0:
                prev_level[i // 2].left = node
            else:
                prev_level[i // 2].right = node

        prev_level = level
        level_start_idx += (2 ** level_num)
        level_num += 1

    return root


# noinspection PyProtectedMember,PyTypeChecker
def pretty_print(root: TreeNode) -> str:
    return '\n'.join(binarytree._build_tree_string(root, 0)[0])
