"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3564/

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right]
coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:
Input: [3,1,5,8]
Output: 167

Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
from typing import List


def max_coins(nums: List[int]) -> int:
    sm = 0
    ln = len(nums)
    nums_sorted = sorted(nums)
    for n in nums_sorted:
        if len(nums) <= 3:
            break

        for i, j in enumerate(nums):
            if j == n:
                sm += j * (1 if i == 0 else nums[i-1]) * (1 if i == ln else nums[i+1])
                nums.pop(i)
                break

    if len(nums) == 3:
        sm += nums[0] * nums[1] * nums[2]
        nums.pop(1)

    if len(nums) == 2:
        sm += nums[0] * nums[1]
        nums.pop(0 if nums[0] < nums[1] else 1)

    if len(nums) == 1:
        sm += nums[0]
        nums.pop()

    return sm

    # sm = 0
    # ln = len(nums)
    # val_to_idx = {n: i for i, n in enumerate(nums)}
    # for n, i in sorted(val_to_idx.items()):
    #     sm += nums[i] * (1 if i == 0 else nums[i-1]) * (1 if i == ln else nums[i+1])
    #
    #
    # return 0


print(max_coins([9, 76, 64, 21]))
