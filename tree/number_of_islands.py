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


def num_islands(grid: List[List[str]]) -> int:
    def explore_island(start_ri, start_ci):
        grid[ri][ci] = '2'
        pass

    island_counter = 0
    for ri, row in enumerate(grid):
        for ci, col in enumerate(row):
            if grid[ri][ci] == '-1':
                island_counter += 1
                explore_island(ri, ci)
