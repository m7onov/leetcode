"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does
not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: false

Constraints:
1 <= n <= 2^31 - 1
"""
from typing import Tuple


class Solution:
    def is_happy(self, n: int) -> bool:
        def advance(cn) -> int:
            res = 0
            for c in str(cn):
                res += int(c) ** 2
            return res

        seen = set()
        num = n
        while num != 1 and num not in seen:
            if num < 100:
                seen.add(num)
            num = advance(num)

        return num == 1


def tests():
    sol = Solution()
    res = sol.is_happy(19)
    print(res)
    res = sol.is_happy(2)
    print(res)


tests()
