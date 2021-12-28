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
import random
from typing import List

# NOTE: see also game_of_life/engine.py


def log(msg):
    # print(msg)
    pass


class Solution:
    def game_of_life(self, board: List[List[int]]):
        cache = dict()
        max_cache_size = 0
        num_rows = len(board)
        num_cols = len(board[0])

        def get_cell(row, col):
            if (row, col) in cache:
                entry = cache[row, col]
                log(f'reduce cache counter: ({row}, {col}): {entry[1]} -> {entry[1] - 1}')
                entry[1] -= 1
                if entry[1] == 0:
                    log(f'pop from cache: ({row}, {col})')
                    cache.pop((row, col))
                return entry[0]
            elif 0 <= row < num_rows and 0 <= col < num_cols:
                return board[row][col]
            else:
                return 0

        def set_cell(row, col, value):
            # NOTE: this function is tied to traverse method, e.g. update_row_by_row()
            prev, board[row][col] = board[row][col], value
            counter = 4
            if col == 0:
                counter -= 1
            elif col == (num_cols - 1):
                counter -= 2

            if row == (num_rows - 1):
                if col == 0:
                    counter -= 2
                else:
                    counter -= 3

            if value != prev:
                log(f'add to cache: ({row}, {col}): {prev}, {counter}')
                cache[row, col] = [prev, counter]

        def get_new_value(row, col, current_value):
            num_lives = 0
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if not (i == 0 and j == 0):
                        cell_value = get_cell(row + i, col + j)
                        num_lives += cell_value
            if current_value == 1:
                if num_lives == 2 or num_lives == 3:
                    return 1
            else:
                if num_lives == 3:
                    return 1
            return 0

        def update_cell(row, col):
            old_value = board[row][col]
            new_value = get_new_value(row, col, old_value)
            log(f'updating ({row}, {col}): {old_value} --> {new_value}')
            set_cell(row, col, new_value)

        def update_row_by_row():
            nonlocal max_cache_size
            for row_idx in range(num_rows):
                for col_idx in range(num_cols):
                    update_cell(row_idx, col_idx)
                    max_cache_size = max(max_cache_size, len(cache))

        update_row_by_row()
        log(f'max_cache_size = {max_cache_size}')
        log(f'cache = {cache}')


def test():
    sol = Solution()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    print('\n'.join(str(r) for r in board))
    sol.game_of_life(board)
    print('')
    print('\n'.join(str(r) for r in board))
    #
    # print('-----------')
    # board = [[1, 1], [1, 0]]
    # print('\n'.join(str(r) for r in board))
    # print('')
    # sol.game_of_life(board)
    # print('\n'.join(str(r) for r in board))
    #
    # cell_values = (0, 1)
    # board = [[random.choice(cell_values) for _ in range(100)] for _ in range(200)]
    # print('\n'.join(str(r) for r in board))
    # sol.game_of_life(board)
    # print('')
    # print('\n'.join(str(r) for r in board))


test()
