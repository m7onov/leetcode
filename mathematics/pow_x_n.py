"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/818/

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
-10^4 <= xn <= 10^4
"""


class Solution:
    def my_pow(self, x: float, n: int) -> float:
        # too slow for large n
        res = 1.0
        for i in range(abs(n)):
            if n < 0:
                res /= x
            else:
                res *= x
        return res

    def my_pow_2(self, x: float, n: int):
        cache = dict()

        def pow_recursive(b: float, e: int):
            if e in cache:
                return cache[e]

            n_abs = abs(e)
            if n_abs > 1:
                p1 = n_abs // 2
                p2 = n_abs - p1
                r1 = pow_recursive(b, p1)
                r2 = pow_recursive(b, p2)
                r3 = b if e > (p1 + p2) else 1
                res = r1 * r2 * r3
                if e < 0:
                    res = 1 / res
            else:
                if e < 0:
                    res = 1 / b
                elif e > 0:
                    res = b
                else:
                    res = 1.0

            cache[e] = res
            return res

        return pow_recursive(x, n)


def tests():
    sol = Solution()
    res = sol.my_pow_2(2.0, 10)
    print(res)
    print('--------------------------')
    res = sol.my_pow_2(2.1, 3)
    print(res)
    print('--------------------------')
    res = sol.my_pow_2(2.0, -2)
    print(res)
    print('--------------------------')
    res = sol.my_pow_2(0.0, 2)
    print(res)
    print('--------------------------')
    res = sol.my_pow_2(0.0, 0)
    print(res)
    print('--------------------------')
    res = sol.my_pow_2(1.0, 0)
    print(res)
    print('--------------------------')
    res = sol.my_pow_2(1.0, 3)
    print(res)
    print('--------------------------')
    res = sol.my_pow_2(1.0, -3)
    print(res)
    print('--------------------------')
    res = sol.my_pow_2(-2.0, -4)
    print(res)
    print('--------------------------')


tests()
