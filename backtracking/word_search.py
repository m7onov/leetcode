"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/797/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

.. image:: https://assets.leetcode.com/uploads/2020/11/04/word2.jpg

Input: board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = 'ABCCED'
Output: true

Example 2:

.. image:: https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg

Input: board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = 'SEE'
Output: true

Example 3:

.. image:: https://assets.leetcode.com/uploads/2020/10/15/word3.jpg

Input: board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = 'ABCB'
Output: false

Constraints:
    | m == board.length
    | n = board[i].length
    | 1 <= m, n <= 6
    | 1 <= word.length <= 15
    | board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = []
        visited = set()

        def check(i, j, wi=0):
            if wi == 0:
                path.clear()
                visited.clear()
            elif wi == len(word):
                print(f'path = {path}')
                return True

            if not 0 <= i < len(board) \
                    or not 0 <= j < len(board[0]) \
                    or not board[i][j] == word[wi] \
                    or (i, j) in visited:
                return False

            visited.add((i, j))
            path.append((i, j))

            if check(i+1, j, wi+1) \
                    or check(i-1, j, wi+1) \
                    or check(i, j+1, wi+1) \
                    or check(i, j-1, wi+1):
                return True
            else:
                visited.remove((i, j))
                path.pop()
                return False

        for ri in range(len(board)):
            for ci in range(len(board[0])):
                if check(ri, ci):
                    return True

        return False


def tests():
    sol = Solution()
    res = sol.exist(
        [['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']], 'ABCCED')
    print(res)

    sol = Solution()
    res = sol.exist(
        [['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']], 'SEE')
    print(res)

    sol = Solution()
    res = sol.exist(
        [['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']], 'ABCB')
    print(res)

    sol = Solution()
    res = sol.exist(
        [['C', 'A', 'A'],
         ['A', 'A', 'A'],
         ['B', 'C', 'D']], 'AAB')
    print(res)

    sol = Solution()
    res = sol.exist(
        [['A', 'B', 'C', 'E'],
         ['S', 'F', 'E', 'S'],
         ['A', 'D', 'E', 'E']], 'ABCESEEEFS')
    print(res)


tests()
