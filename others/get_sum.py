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
from others import bin_format


class Solution:
    def get_sum_1(self, a: int, b: int) -> int:
        # will not work for big a or b
        return round(log2(2**a * 2**b))

    def get_sum_2(self, a: int, b: int) -> int:
        print(f'{bin_format(a):>40s}', f'{bin_format(b):>40s}')
        while b & 0xFFFF != 0:
            t = a ^ b
            b = (a & b) << 1
            a = t
            print(f'{bin_format(a):>40s}', f'{bin_format(b):>40s}')

        if (a & 0xFFFF) <= 0x7FFF:
            a = a & 0xFFFF

        return a


def tests():
    sol = Solution()
    res = sol.get_sum_2(37, 95)
    print(res)
    res = sol.get_sum_2(37, 0)
    print(res)
    res = sol.get_sum_2(0, 95)
    print(res)
    res = sol.get_sum_2(0, 0)
    print(res)
    res = sol.get_sum_2(95, -37)
    print(res)
    res = sol.get_sum_2(37, -95)
    print(res)
    res = sol.get_sum_2(2, -3)
    print(res)
    res = sol.get_sum_2(-37, -57)
    print(res)


tests()
