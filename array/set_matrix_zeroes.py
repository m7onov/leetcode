"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
You must do it in place.

Example 1:
.. image:: https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
.. image:: https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1

Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        zero_row_idxs = set()
        zero_col_idxs = set()
        for ri in range(num_rows):
            for ci in range(num_cols):
                if matrix[ri][ci] == 0:
                    zero_row_idxs.add(ri)
                    zero_col_idxs.add(ci)

        for ri in range(num_rows):
            for ci in range(num_cols):
                if ri in zero_row_idxs or ci in zero_col_idxs:
                    matrix[ri][ci] = 0

    def setZeroesConstantSpace(self, matrix: List[List[int]]) -> None:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        indicator_row_idx = None
        indicator_col_idx = None
        for ri in range(num_rows):
            for ci in range(num_cols):
                if matrix[ri][ci] == 0:
                    # print(ri, ci, '(', indicator_row_idx, indicator_col_idx, ')', ' = ', 0)
                    if indicator_row_idx is None:
                        indicator_row_idx = ri
                        indicator_col_idx = ci
                        for i in range(num_cols):
                            matrix[ri][i] = 0 if matrix[ri][i] != 0 else 1
                        for i in range(num_rows):
                            matrix[i][ci] = 0 if matrix[i][ci] != 0 else 1
                    elif ri != indicator_row_idx and ci != indicator_col_idx:
                        # print('set')
                        matrix[ri][indicator_col_idx] = 1
                        matrix[indicator_row_idx][ci] = 1

        if indicator_row_idx is None:
            return

        # print('\n'.join(str(m) for m in matrix))

        for ri in range(num_rows):
            for ci in range(num_cols):
                if ri != indicator_row_idx and ci != indicator_col_idx:
                    if matrix[ri][indicator_col_idx] == 1 or matrix[indicator_row_idx][ci] == 1:
                        matrix[ri][ci] = 0

        for i in range(num_cols):
            matrix[indicator_row_idx][i] = 0

        for i in range(num_rows):
            matrix[i][indicator_col_idx] = 0


sol = Solution()

# indata = [[1, 1, 1],
#           [1, 0, 1],
#           [1, 1, 1]]
# sol.setZeroes(indata)
# print(indata)
#
# indata = [[0, 1, 2, 0],
#           [3, 4, 5, 2],
#           [1, 3, 1, 5]]
# sol.setZeroes(indata)
# print(indata)

# indata = [[1, 1, 1],
#           [1, 0, 1],
#           [1, 1, 1]]
# sol.setZeroesConstantSpace(indata)
# print(indata)

# indata = [[0, 1, 2, 0],
#           [3, 4, 5, 2],
#           [1, 3, 1, 5]]
# sol.setZeroesConstantSpace(indata)
# print(indata)

indata = [[1, 2, 3, 4],
          [5, 0, 7, 8],
          [0, 10, 11, 12],
          [13, 14, 15, 0]]
sol.setZeroesConstantSpace(indata)
print(indata)
