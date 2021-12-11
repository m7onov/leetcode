"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/822/

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5

Constraints:
-1000 <= a, b <= 1000
"""
from math import log2


class Solution:
    def get_sum(self, a: int, b: int) -> int:
        return round(log2(2**a * 2**b))


def tests():
    sol = Solution()
    res = sol.get_sum(2, -999)
    print(res)


tests()
