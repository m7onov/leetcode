"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/880/

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0
"""


def reverse(x: int) -> int:
    abs_x = abs(x)

    if abs_x < 10:
        return x

    x_str = []
    for n in range(15):
        v1 = abs_x // pow(10, n)
        if v1 == 0:
            break
        else:
            v2 = v1 % 10
            x_str.append(str(v2))

    ln = len(x_str)
    max_val = pow(2, 31) - 1
    ret_val = 0
    for i in range(ln):
        v = int(x_str[ln - i - 1]) * pow(10, i)
        if max_val - ret_val < v:
            return 0

        ret_val += v

    return ret_val * (-1 if x < 0 else 1)

