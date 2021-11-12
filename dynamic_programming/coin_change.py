"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/809/

You are given an integer array coins representing coins of different denominations and an integer amount representing
a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by
any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Example 4:
Input: coins = [1], amount = 1
Output: 1

Example 5:
Input: coins = [1], amount = 2
Output: 2

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
"""
from typing import List
from math import inf


class Solution:
    def coin_change_1(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        memo_table = [0] * amount
        for a in range(1, amount + 1):
            min_path = inf
            for j, c in enumerate(coins):
                if c <= a:
                    min_path = min(min_path, memo_table[a - c - 1] + 1)

            memo_table[a-1] = min_path

        # print(memo_table)
        return memo_table[-1] if memo_table[-1] != inf else -1


def tests():
    sol = Solution()
    res = sol.coin_change_1([1, 2, 5], 11)
    print(res)
    res = sol.coin_change_1([2], 3)
    print(res)
    res = sol.coin_change_1([1], 0)
    print(res)
    res = sol.coin_change_1([1], 1)
    print(res)
    res = sol.coin_change_1([1], 2)
    print(res)


tests()
