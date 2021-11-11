"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/806/

Write an efficient algorithm that searches for a target value in an m x n integer matrix.
The matrix has the following properties:
    - Integers in each row are sorted in ascending from left to right.
    - Integers in each column are sorted in ascending from top to bottom.

Example 1:

.. image:: https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg


| Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
| Output: true
|

Example 2:

.. image:: https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg

| Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
| Output: false
|

Constraints:
    - m == matrix.length
    - n == matrix[i].length
    - 1 <= n, m <= 300
    - -10^9 <= matrix[i][j] <= 10^9
    - All the integers in each row are sorted in ascending order.
    - All the integers in each column are sorted in ascending order.
    - -10^9 <= target <= 10^9
"""
from typing import List


class Solution:
    def search_matrix_0(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == target:
                    return True
        return False

    def search_matrix_1(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        def bin_search(start_idx, end_idx, el_getter):
            if start_idx == end_idx:
                return el_getter(start_idx) == target

            middle_idx = (start_idx + end_idx) // 2
            if el_getter(middle_idx) >= target:
                return bin_search(start_idx, middle_idx, el_getter)
            else:
                return bin_search(middle_idx+1, end_idx, el_getter)

        def circle_getter1(circle_idx, idx):
            circle_cols = num_cols - 2 * circle_idx
            row_idx = circle_idx + (0 if idx < circle_cols else (idx - circle_cols + 1))
            col_idx = circle_idx + (idx if idx < circle_cols else (circle_cols - 1))
            return matrix[row_idx][col_idx]

        def circle_getter2(circle_idx, idx):
            circle_rows = num_rows - 2 * circle_idx
            row_idx = circle_idx + (idx if idx < circle_rows else (circle_rows - 1))
            col_idx = circle_idx + (0 if idx < circle_rows else (idx - circle_rows + 1))
            return matrix[row_idx][col_idx]

        def bin_search_in_circle(circle_idx):
            circle_len = num_rows + num_cols - 1 - 4*circle_idx
            if bin_search(0, circle_len - 1, lambda x: circle_getter1(circle_idx, x)):
                return True
            else:
                return bin_search(0, circle_len - 1, lambda x: circle_getter2(circle_idx, x))

        min_len = min(len(matrix), len(matrix[0]))
        circles = min_len // 2 + (min_len % 2)
        for ci in range(circles):
            if bin_search_in_circle(ci):
                return True

        return False

    def search_matrix_2(self, matrix: List[List[int]], target: int) -> bool:
        # divide matrix to 4 smaller matrices then search recursive
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        def search_recursive(from_row_idx, to_row_idx, from_col_idx, to_col_idx) -> bool:
            if from_row_idx == to_row_idx and from_col_idx == to_col_idx:
                return matrix[from_row_idx][from_col_idx] == target

            row_middle_idx = (from_row_idx + to_row_idx) // 2
            col_middle_idx = (from_col_idx + to_col_idx) // 2

            print(f'from_row_idx = {from_row_idx}, to_row_idx = {to_row_idx}, '
                  f'from_col_idx = {from_col_idx}, to_col_idx = {to_col_idx}, '
                  f'row_middle_idx = {row_middle_idx}, col_middle_idx = {col_middle_idx}')

            if matrix[from_row_idx][from_col_idx] <= target <= matrix[row_middle_idx][col_middle_idx]:
                # top left block
                if search_recursive(from_row_idx, row_middle_idx, from_col_idx, col_middle_idx):
                    return True

            if row_middle_idx < to_row_idx and col_middle_idx < to_col_idx and \
                    matrix[row_middle_idx + 1][col_middle_idx + 1] <= target <= matrix[to_row_idx][to_col_idx]:
                # bottom right block
                if search_recursive(row_middle_idx + 1, to_row_idx, col_middle_idx + 1, to_col_idx):
                    return True

            if row_middle_idx < to_row_idx and \
                    matrix[row_middle_idx+1][from_col_idx] <= target <= matrix[to_row_idx][col_middle_idx]:
                # bottom left block
                if search_recursive(row_middle_idx+1, to_row_idx, from_col_idx, col_middle_idx):
                    return True

            if col_middle_idx < to_col_idx and \
                    matrix[from_row_idx][col_middle_idx+1] <= target <= matrix[row_middle_idx][to_col_idx]:
                # top right block
                if search_recursive(from_row_idx, row_middle_idx, col_middle_idx+1, to_col_idx):
                    return True

            return False

        return search_recursive(0, num_rows - 1, 0, num_cols - 1)

    def searh_matrix_3(self, matrix: List[List[int]], target: int) -> bool:
        # TODO: search space reduction
        pass


def tests():
    sol = Solution()
    res = sol.search_matrix_2([[1,   4,  7, 11, 15],
                               [2,   5,  8, 12, 19],
                               [3,   6,  9, 16, 22],
                               [10, 13, 14, 17, 24],
                               [18, 21, 23, 26, 30]], 5)
    print(res)


tests()
