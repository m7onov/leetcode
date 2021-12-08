"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/820/

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345
would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed
integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1,
then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Example 3:
Input: dividend = 0, divisor = 1
Output: 0

Example 4:
Input: dividend = 1, divisor = 1
Output: 1

Constraints:
-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # too slow
        cnt = 0
        res = abs(dividend)
        while res > 0:
            res = res - abs(divisor)
            if res >= 0:
                cnt += 1

        if dividend > 0 > divisor or divisor > 0 > dividend:
            cnt = -cnt

        return cnt

    def divide_2(self, dividend: int, divisor: int) -> int:
        # no overflow handling
        divd_abs = abs(dividend)
        divs_abs = abs(divisor)
        parts = [(divs_abs, 1)]
        res = divd_abs
        cnt = 0
        while abs(res) >= divs_abs or res < 0:
            print(f'res = {res}, cnt = {cnt}, parts[-1] = {parts[-1]}')
            if res < 0:
                parts.pop()
                part = parts[-1]
                res += part[0]
                cnt -= part[1]
            else:
                part = parts[-1]
                res -= part[0]
                cnt += part[1]
                if res > 0:
                    parts.append((part[0] + part[0], part[1] + part[1]))

        if dividend > 0 > divisor or divisor > 0 > dividend:
            cnt = -cnt

        return cnt

    def divide_3(self, dividend: int, divisor: int) -> int:
        max_val = 2**31 - 1
        divd_abs = abs(dividend)
        divs_abs = abs(divisor)
        is_negative = dividend > 0 > divisor or divisor > 0 > dividend
        parts = [(divs_abs, 1)]
        res = divd_abs
        cnt = 0
        while res >= divs_abs:
            # print(f'res = {res :>15}, cnt = {cnt :>15}, parts[-1] = ({parts[-1][0] :>15}, {parts[-1][1] :>15})')
            part = parts[-1]

            if not is_negative:
                if max_val - part[1] < cnt:
                    return max_val

            res -= part[0]
            cnt += part[1]
            if max_val - part[0] - part[0] >= cnt:
                parts.append((part[0] + part[0], part[1] + part[1]))

            # print(f'res = {res :>15}, cnt = {cnt :>15}, parts[-1] = ({parts[-1][0] :>15}, {parts[-1][1] :>15})')

            while len(parts) > 0 and parts[-1][0] > res:
                part = parts.pop()
                rem_part = parts[-1] if len(parts) > 0 else None
                # print(f'remove part = {part}, remain part = {rem_part}')

        if is_negative:
            cnt = -cnt

        return cnt


def tests():
    sol = Solution()
    res = sol.divide_3(10, 3)
    print(res)
    res = sol.divide_3(7, -3)
    print(res)
    res = sol.divide_3(0, 1)
    print(res)
    res = sol.divide_3(1, 1)
    print(res)
    res = sol.divide_3(-1, 1)
    print(res)
    res = sol.divide_3(1000000, 3)
    print(res)
    res = sol.divide_3(-2147483648, -1)
    print(res)
    res = sol.divide_3(2147483648, -1)
    print(res)


tests()
