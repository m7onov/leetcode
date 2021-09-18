from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_full_str(self, ident=2, ident_total=0):
        left_str = ''
        if self.left is not None:
            left_str = ('\n' + ((ident_total + ident) * ' ') + 'l - '
                        + self.left.to_full_str(ident, ident_total + ident))

        right_str = ''
        if self.right is not None:
            right_str = ('\n' + ((ident_total + ident) * ' ') + 'r - '
                         + self.right.to_full_str(ident, ident_total + ident))

        return str(self.val) + left_str + right_str

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
