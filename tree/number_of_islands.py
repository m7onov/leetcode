"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/792/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
    | m == grid.length
    | n == grid[i].length
    | 1 <= m, n <= 300
    | grid[i][j] is '0' or '1'.
"""
from typing import List


def num_islands1(grid: List[List[str]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])

    def explore(start_ri, start_ci):
        stack = [(start_ri, start_ci)]
        while len(stack) > 0:
            rc = stack.pop()

            if grid[rc[0]][rc[1]] == '1':
                grid[rc[0]][rc[1]] = '2'
            else:
                continue

            if rc[1] < num_cols - 1:
                stack.append((rc[0], rc[1] + 1))
            if rc[0] < num_rows - 1:
                stack.append((rc[0] + 1, rc[1]))
            if rc[1] > 0:
                stack.append((rc[0], rc[1] - 1))
            if rc[0] > 0:
                stack.append((rc[0] - 1, rc[1]))

    island_counter = 0
    for ri, row in enumerate(grid):
        for ci, col in enumerate(row):
            if grid[ri][ci] == '1':
                island_counter += 1
                explore(ri, ci)

    return island_counter


def num_islands2(grid: List[List[str]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])

    def explore(start_ri, start_ci):
        stack = [(start_ri, start_ci)]
        while len(stack) > 0:
            new_stack = []
            for rc in stack:
                if grid[rc[0]][rc[1]] == '1':
                    grid[rc[0]][rc[1]] = '2'
                    if rc[1] < num_cols - 1:
                        new_stack.append((rc[0], rc[1] + 1))
                    if rc[0] < num_rows - 1:
                        new_stack.append((rc[0] + 1, rc[1]))
                    if rc[1] > 0:
                        new_stack.append((rc[0], rc[1] - 1))
                    if rc[0] > 0:
                        new_stack.append((rc[0] - 1, rc[1]))

            stack = new_stack

    island_counter = 0
    for ri, row in enumerate(grid):
        for ci, col in enumerate(row):
            if grid[ri][ci] == '1':
                island_counter += 1
                explore(ri, ci)

    return island_counter


res = num_islands2([
  ['1', '1', '1', '1', '0'],
  ['1', '1', '0', '1', '0'],
  ['1', '1', '0', '0', '0'],
  ['0', '0', '0', '0', '0']
])
print(res)

res = num_islands2([
  ['1', '1', '0', '0', '0'],
  ['1', '1', '0', '0', '0'],
  ['0', '0', '1', '0', '0'],
  ['0', '0', '0', '1', '1']
])
print(res)
