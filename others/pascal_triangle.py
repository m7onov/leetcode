"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif


Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30
"""
from typing import List


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        triangle = [[1]]
        for ri in range(num_rows-1):
            pa = [0] + triangle[-1] + [0]
            ca = [(pa[j-1] + pa[j]) for j in range(1, len(pa))]
            triangle.append(ca)

        return triangle


sol = Solution()
ans = sol.generate(30)

print('\n'.join([str(r) for r in ans]))
