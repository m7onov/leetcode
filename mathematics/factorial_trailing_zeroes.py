"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/816/

Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
Input: n = 0
Output: 0

Constraints:
0 <= n <= 10^4

Follow up: Could you write a solution that works in logarithmic time complexity?
"""


class Solution:
    def trailing_zeroes(self, n: int) -> int:
        def count_factors(n_factorial, start_factor) -> int:
            power = 1
            counter = 0
            while True:
                factor = start_factor ** power
                factor_counter = n // factor
                if factor_counter <= 0:
                    break
                counter += factor_counter
                power += 1
            return counter

        num_2 = count_factors(n, 2)
        num_5 = count_factors(n, 5)
        return min(num_2, num_5)


def tests():
    sol = Solution()
    res = sol.trailing_zeroes(3)
    print(res)
    res = sol.trailing_zeroes(5)
    print(res)
    res = sol.trailing_zeroes(0)
    print(res)


tests()
