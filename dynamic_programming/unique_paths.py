"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/808/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

.. image:: https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png

Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:
Input: m = 7, n = 3
Output: 28

Example 4:
Input: m = 3, n = 3
Output: 6

Constraints:
1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10^9.
"""
from math import factorial, comb


class Solution:
    def unique_paths_1(self, m: int, n: int) -> int:
        memo_table = [[0] * n for _ in range(m)]
        memo_table[0][0] = 1
        for c in range(n):
            for r in range(m):
                a = memo_table[r - 1][c] if r > 0 else 0
                b = memo_table[r][c - 1] if c > 0 else 0
                memo_table[r][c] += a + b

        # print('\n'.join([str(x) for x in memo_table]))
        return memo_table[-1][-1]

    def unique_paths_2(self, m: int, n: int) -> int:
        """
        NOTE: Полная длина пути всегда будет равна n - 1 + m - 1.
              Это можно представить себе как множество номеров шагов {1 .. (n - 1 + m - 1)}.
              Различные пути образуются в результате того, что из этого множества мы выбираем различные
                подмножества размера (n - 1) или (m - 1). Выбранное подмножество шагов соответствует номерам
                шагов на которых мы двигаемся вправо или влево. Порядок выборки элементов не имеет значения,
                так как не влияет на соответствующий путь. Например, если в первом случае выбраны эелменты {3, 4},
                а во втором элементы {4, 3} это будет обозначать один и тот же путь -
                "на 3-ем и 4-ом шаге повернуть направо". Это соответствут формуле числа сочетаний из n по k
                https://ru.wikipedia.org/wiki/Сочетание
        """
        return comb(n - 1 + m - 1, n - 1)


def tests():
    sol = Solution()
    res = sol.unique_paths_2(3, 7)
    print(res)
    res = sol.unique_paths_2(3, 2)
    print(res)
    res = sol.unique_paths_2(7, 3)
    print(res)
    res = sol.unique_paths_2(3, 3)
    print(res)


tests()
