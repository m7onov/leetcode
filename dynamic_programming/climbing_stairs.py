"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""


def climb_stairs(n: int) -> int:
    cur_c, n1, n2 = 0, 0, 0
    for i in range(n):
        if i == 0:
            cur_c = 1
            n1 = 1

        elif i == 1:
            cur_c = 2
            n2 = 2

        else:
            cur_c = n1 + n2
            n1 = n2
            n2 = cur_c

    return cur_c


print(climb_stairs(3))
