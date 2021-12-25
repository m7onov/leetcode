"""
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/828/

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

.. image:: https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

.. image:: https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List
from math import ceil


class Solution:
    def spiral_order_2(self, matrix: List[List[int]]) -> List[int]:
        ret_list = []
        print('\n'.join(str(i) for i in matrix))
        rows = len(matrix)
        cols = len(matrix[0])
        turn_num = min(ceil(rows / 2), ceil(cols / 2))
        for turn_idx in range(turn_num):
            turn_rows = rows - 2 * turn_idx
            turn_cols = cols - 2 * turn_idx
            print(f'turn_rows = {turn_rows}')
            print(f'turn_cols = {turn_cols}')
            print(f'O: ({turn_idx}, {turn_idx})')
            ret_list.append(matrix[turn_idx][turn_idx])
            if turn_cols > 1:
                for i in range(1, turn_cols):
                    print(f'A: ({turn_idx}, {turn_idx + i})')
                    ret_list.append(matrix[turn_idx][turn_idx + i])
            if turn_rows > 1:
                for i in range(1, turn_rows):
                    print(f'B: ({turn_idx + i}, {turn_idx + turn_cols - 1})')
                    ret_list.append(matrix[turn_idx + i][turn_idx + turn_cols - 1])
            if turn_rows > 1 and turn_cols > 1:
                for i in range(1, turn_cols):
                    print(f'C: ({turn_idx + turn_rows - 1}, {turn_idx + turn_cols - 1 - i})')
                    ret_list.append(matrix[turn_idx + turn_rows - 1][turn_idx + turn_cols - 1 - i])
            if turn_rows > 1 and turn_cols > 1:
                for i in range(1, turn_rows - 1):
                    print(f'D: ({turn_idx + turn_rows - 1 - i}, {turn_idx})')
                    ret_list.append(matrix[turn_idx + turn_rows - 1 - i][turn_idx])
        return ret_list


def test():
    sol = Solution()
    sol.spiral_order_2([[0] * 3 for _ in range(6)])
    sol = Solution()
    sol.spiral_order_2([[0] * 6 for _ in range(3)])
    sol = Solution()
    sol.spiral_order_2([[0] * 6 for _ in range(2)])
    sol = Solution()
    sol.spiral_order_2([[0] * 1 for _ in range(1)])


test()
