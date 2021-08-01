"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/

Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3^x.

Example 1:
Input: n = 27
Output: true

Example 2:
Input: n = 0
Output: false

Example 3:
Input: n = 9
Output: true

Example 4:
Input: n = 45
Output: false

Constraints:
-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def __init__(self):
        self.ps = {1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907,
                   43046721, 129140163, 387420489, 1162261467}

    def is_power_of_three(self, n: int) -> bool:
        return n in self.ps

    def is_power_of_three2(self, n: int) -> bool:
        return (n > 0) and (1162261467 % n == 0)


print(Solution().is_power_of_three2(27))
print(Solution().is_power_of_three2(0))
print(Solution().is_power_of_three2(9))
print(Solution().is_power_of_three2(45))
