from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def to_full_str(self, ident=0):
        left_str = self.left.to_full_str(ident+1) if self.left is not None else 'None'
        right_str = self.right.to_full_str(ident+1) if self.right is not None else 'None'

        return str(self.val) + '\n' + (2*ident*' ') + 'left: ' + left_str + '\n' + (2*ident*' ') + 'right: ' + right_str

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
