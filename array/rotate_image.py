"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/770/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:
Input: matrix = [[1]]
Output: [[1]]

Example 4:
Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]
"""
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)

    def get_substitution_value_for(dr: str, row_idx: int, col_idx: int) -> (int, int, int):
        if dr == 'west':
            return matrix[n - 1 - col_idx][row_idx], n - 1 - col_idx, row_idx
        elif dr == 'south':
            return matrix[n - 1 - col_idx][row_idx], n - 1 - col_idx, row_idx
        elif dr == 'east':
            return matrix[n - 1 - col_idx][row_idx], n - 1 - col_idx, row_idx
        else:
            raise Exception('unknown dr:', dr)

    for r in range(n // 2):
        for c in range(r, n - r - 1):
            north_v, o_r, o_c = matrix[r][c], r, c
            n_v, n_r, n_c = get_substitution_value_for('west', o_r, o_c)
            matrix[o_r][o_c] = n_v
            o_r, o_c = n_r, n_c
            n_v, n_r, n_c = get_substitution_value_for('south', o_r, o_c)
            matrix[o_r][o_c] = n_v
            o_r, o_c = n_r, n_c
            n_v, n_r, n_c = get_substitution_value_for('east', o_r, o_c)
            matrix[o_r][o_c] = n_v
            matrix[n_r][n_c] = north_v


# TODO: transpose then reverse
