"""
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/831/

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the
British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or
dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using
the following four rules (taken from the above Wikipedia article):
    1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by over-population.
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births
and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Example 1:

.. image:: https://assets.leetcode.com/uploads/2020/12/26/grid1.jpg

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:

.. image:: https://assets.leetcode.com/uploads/2020/12/26/grid2.jpg

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.

Follow up:
    - Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some
      cells first and then use their updated values to update other cells.
    - In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause
      problems when the active area encroaches upon the border of the array (i.e., live cells reach the border).
      How would you address these problems?
"""
from typing import List


class Solution:
    def game_of_life(self, board: List[List[int]]):
        window = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        window[1][1] = board[0][0]
        window[1][2] = board[0][1]
        window[2][2] = board[1][1]
        window[2][1] = board[1][0]

        def update():
            num_lives = sum(window[0]) + sum(window[2]) + window[1][0] + window[1][2]
            if window[1][1] == 1:
                if num_lives == 2 or num_lives == 3:
                    return 1
            else:
                if num_lives == 3:
                    return 1
            return 0

        def get_neighbor(r, c, w_r, w_c, where):
            if where == 'tl':
                return r + w_r - 1, c + w_c - 1
            elif where == 'tc':
                return w_r - 1, w_c
            elif where == 'tr':
                return w_r - 1, w_c + 1
            pass

        def move_window(r, c, direction):
            pass

        num_rows = len(board)
        num_cols = len(board[0])
        for i in range(num_rows):
            for j in range(num_cols):
                new_val = update()
                board[i][j] = new_val
