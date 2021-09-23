"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3559/

You are given a list of songs where the ith song has a duration of time[i] seconds.
Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the
number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

Example 1:
Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:
Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.

Constraints:
1 <= time.length <= 6 * 104
1 <= time[i] <= 500
"""
from typing import List
from mathematics import factorial
from collections import defaultdict


def num_pairs_divisible_by_60_mathy(time: List[int]) -> int:
    pairs = [0 for _ in range(60)]
    for t in time:
        tr = t % 60
        pairs[tr] += 1

    # для остатка 0 и 30 нужно посчитать количество сочетаний из pairs[0,30] по 2
    ret_num = 0
    for j in [0, 30]:
        if pairs[j] >= 2:
            ret_num += (factorial(pairs[j]) // factorial(pairs[j] - 2) // 2)

    # для остальных нужно умножить pairs[i] на pairs[-i]
    for i in range(1, 30):
        ret_num += (pairs[i] * pairs[-i])

    return ret_num


def num_pairs_divisible_by_60_elegant(time: List[int]) -> int:
    remainders = defaultdict(int)
    ret = 0
    for t in time:
        if t % 60 == 0:
            ret += remainders[0]  # make a pair with all elements that are equal to 0 modulo 60

        else:
            ret += remainders[60 - t % 60]  # make pair with all elements that have remainder equals 60 - remainder of t

        remainders[t % 60] += 1  # remember the remainder of current element

    return ret


print(num_pairs_divisible_by_60_mathy([30, 20, 150, 100, 40]))
print(num_pairs_divisible_by_60_mathy([60, 60, 60]))


# TODO: what if we need 3 songs with total duration divisible by 60 or some other number?
