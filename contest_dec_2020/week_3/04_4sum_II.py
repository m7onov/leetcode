"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3569/

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that
A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range
of -2^28 to 2^28 - 1 and the result is guaranteed to be at most 2^31 - 1.

Example:
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""
from collections import defaultdict
from typing import List


def four_sum_count(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    sm1 = defaultdict(int)
    for i in a:
        for j in b:
            sm1[i+j] += 1

    sm2 = defaultdict(int)
    for i in c:
        for j in d:
            sm2[i+j] += 1

    cnt = 0
    for n, c in sm1.items():
        cnt += (c * sm2[-n])

    return cnt


print(four_sum_count([1, 2],
                     [-2, -1],
                     [-1, 2],
                     [0, 2]))

