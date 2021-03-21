"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/576/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
from typing import List, Tuple


def rob(nums: List[int]) -> int:
    # элемент с индексом i - это сумма оптимальной последовательности от n[0] .. n[i]
    # opt_sum = [nums[0], max(nums[0], nums[1])]
    opt_sum = []
    for i, n in enumerate(nums):
        if i == 0:
            opt_sum.append(n)
        elif i == 1:
            opt_sum.append(max(opt_sum[-1], n))
        else:
            v1 = opt_sum[i-2] + n
            v2 = opt_sum[i-1]
            opt_sum.append(max(v1, v2))

    return opt_sum[-1]


def rob_with_path(nums: List[int]) -> Tuple[int, List[int]]:
    # элемент с индексом i - это сумма оптимальной последовательности от n[0] .. n[i]
    # opt_sum = [nums[0], max(nums[0], nums[1])]
    opt_sum = []
    for i, n in enumerate(nums):
        if i == 0:
            opt_sum.append(n)
        elif i == 1:
            opt_sum.append(max(opt_sum[-1], n))
        else:
            v1 = opt_sum[i-2] + n
            v2 = opt_sum[i-1]
            opt_sum.append(max(v1, v2))

    # найти выбранные индексы
    opt_path = []
    i = len(nums)-1
    while i >= 0:
        if i == 0:
            opt_path.append(i)
            i -= 1
        else:
            if opt_sum[i] == opt_sum[i-1]:
                i -= 1
            else:
                opt_path.append(i)
                i -= 2

    opt_path.reverse()
    return opt_sum[-1], opt_path


print(rob([1, 2, 3, 1]))
print(rob([2, 7, 9, 3, 1]))

print(rob_with_path([1, 2, 3, 1]))
print(rob_with_path([2, 7, 9, 3, 1]))
