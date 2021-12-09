"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/819/

Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is
returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.


Constraints:
0 <= x <= 2^31 - 1
"""
from math import ceil, floor


class Solution:
    def my_sqrt(self, x: int) -> int:
        # not effective for big x
        i = x
        while i * i > x:
            i -= 1
        return i

    def my_sqrt_2(self, x) -> int:
        # Newton method
        # https://ru.wikipedia.org/wiki/Метод_Ньютона
        # r is argument of function
        # f(x) = x^2 - r
        # f(x) = 0
        # x[n+1] = x[n] - f(x[n]) / f'(x[n]) = x[n] - (x[n]^2 - r) / (2 * x[n])
        def n_next(a):
            return a - (a * a - x) / (2 * a)

        root = float(x)
        while floor(root) * floor(root) > x:
            root = n_next(root)

        return floor(root)


def tests():
    # sol = Solution()
    # res = sol.my_sqrt(4)
    # print(res)
    # res = sol.my_sqrt(8)
    # print(res)
    sol = Solution()
    res = sol.my_sqrt_2(8)
    print(res)
    res = sol.my_sqrt_2(3.999999999999996)
    print(res)


tests()

