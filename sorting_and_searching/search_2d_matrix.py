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
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        ln_r = len(matrix)
        ln_c = len(matrix[0])

        def bin_search(s_r, s_c, e_r, e_c) -> bool:
            if s_r == e_r:
                return matrix[s_r][s_c] == target

            m = (s_r + e_r) // 2
            if target <= matrix[s_r + m][s_c + m]:
                return bin_search(s_r, s_c, s_r + m, s_c + m)
            else:
                return bin_search(s_r + m + 1, s_c + m + 1, e_r, e_c)

        for i in range(ln_r + ln_c - 1):
            a_r = (ln_r - 1 - i) if i < ln_r else 0
            a_c = 0 if i < ln_r else (i - ln_r + 1)
            b_r = (ln_r - 1) if i < ln_c else (ln_r - 1 - (i - ln_c + 1))
            b_c = i if i < ln_c else (ln_c - 1)
            print(f'({a_r}, {a_c}) - ({b_r}, {b_c})')

            a = matrix[a_r][a_c]
            b = matrix[b_r][b_c]
            if a <= target <= b:
                return bin_search(a_r, a_c, b_r, b_c)

        return False


def tests():
    sol = Solution()
    sol.search_matrix([[1,   4,  7, 11, 15],
                       [2,   5,  8, 12, 19],
                       [3,   6,  9, 16, 22],
                       [10, 13, 14, 17, 24],
                       [18, 21, 23, 26, 30]], 20)
    # sol.search_matrix([[1, 4, 7, 11, 15],
    #                    [2, 5, 8, 12, 19],
    #                    [3, 6, 9, 16, 22]], 20)


tests()
