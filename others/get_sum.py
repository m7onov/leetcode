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
    def get_sum_1(self, a: int, b: int) -> int:
        return round(log2(2**a * 2**b))

    def get_sum_2(self, a: int, b: int) -> int:
        if a >= 0 and b >= 0 or a <= 0 and b <= 0:
            is_negative = a < 0
            while b > 0:
                t = a ^ b
                b = (a & b) << 1
                a = t
            return self.get_sum_2(~a, 1) if is_negative else a
        elif b < 0:
            # b_c = self.get_sum_2(~b, 1)
            # print(f'b_c = {bin(b_c)}')
            return self.get_sum_2(a, b)
        else:
            return self.get_sum_2(b, a)

        return 0


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


tests()
