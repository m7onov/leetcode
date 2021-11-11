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

        i, j = 0, 0
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
        # TODO: divide matrix to 4 smaller matrices then search recursive
        pass

    def searh_matrix_3(self, matrix: List[List[int]], target: int) -> bool:
        # TODO: search space reduction
        pass


def tests():
    sol = Solution()
    res = sol.search_matrix_1([[1,   4,  7, 11, 15],
                               [2,   5,  8, 12, 19],
                               [3,   6,  9, 16, 22],
                               [10, 13, 14, 17, 24],
                               [18, 21, 23, 26, 30]], 9)
    print(res)


tests()
