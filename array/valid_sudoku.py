"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/769/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's
in the top left 3x3 sub-box, it is invalid.
"""
from typing import List


def is_valid_sudoku(board: List[List[str]]) -> bool:
    square_digits = {}
    vline_digits = {}
    hline_digits = {}

    for i in range(len(board)):
        square_digits[i] = set()
        vline_digits[i] = set()
        hline_digits[i] = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.':
                continue

            if board[i][j] in hline_digits[i]:
                print('1')
                return False
            else:
                hline_digits[i].add(board[i][j])

            if board[i][j] in vline_digits[j]:
                print('2')
                return False
            else:
                vline_digits[j].add(board[i][j])

            if board[i][j] in square_digits[3 * (i // 3) + (j // 3)]:
                print('3')
                return False
            else:
                square_digits[3 * (i // 3) + (j // 3)].add(board[i][j])

    return True
