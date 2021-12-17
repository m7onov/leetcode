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
from math import log, exp


class Solution:
    def get_sum(self, a: int, b: int) -> int:
        print(exp(a))
        print(exp(b))
        return round(log(exp(a) * exp(b)))


def tests():
    sol = Solution()
    # res = sol.get_sum(1, 2)
    # print(res)
    # res = sol.get_sum(2, 3)
    # print(res)
    res = sol.get_sum(-999, 0)
    print(res)


tests()
