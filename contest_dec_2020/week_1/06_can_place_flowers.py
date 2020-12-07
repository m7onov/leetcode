"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3555/

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted
in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""
from typing import List


def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    cnt = 0
    for i, f in enumerate(flowerbed):
        # we can imagine an emply plot before the first plot in flowerbed only if the first plot is zero
        if i == 0 and f == 0:
            cnt += 1

        if f == 1:
            cnt = 0
        else:
            cnt += 1

        if cnt == 3:
            n -= 1
            cnt = 1

        if n == 0:
            return True

    # we can imagine an empty plot after the last plot in flowerbed only if there are two empty plots at the end
    if cnt == 2:
        n -= 1

    if n == 0:
        return True

    return False


print(can_place_flowers([1, 0, 0, 0, 0, 0, 1], 2))
