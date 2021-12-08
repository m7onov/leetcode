"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/821/

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
If multiple answers are possible, return any of them.
It is guaranteed that the length of the answer string is less than 10^4 for all the given inputs.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 2, denominator = 3
Output: "0.(6)"

Example 4:
Input: numerator = 4, denominator = 333
Output: "0.(012)"

Example 5:
Input: numerator = 1, denominator = 5
Output: "0.2"

Constraints:
-2^31 <= numerator, denominator <= 2^31 - 1
denominator != 0
"""


class Solution:
    def fraction_to_decimal(self, numerator: int, denominator: int) -> str:
        num_abs = abs(numerator)
        den_abs = abs(denominator)

        result = str(num_abs // den_abs)
        if numerator > 0 > denominator or denominator > 0 > numerator:
            result = '-' + result

        remainder = num_abs % den_abs
        fractional = []

        repeating_start_idx = None
        seen = dict()
        while remainder > 0 and repeating_start_idx is None:
            seen[remainder] = len(fractional)
            while remainder < den_abs:
                remainder = 10 * remainder
                if remainder < den_abs:
                    fractional.append('0')

            fractional.append(str(remainder // den_abs))
            remainder = remainder % den_abs
            if remainder in seen:
                repeating_start_idx = seen[remainder]

        if len(fractional) > 0:
            if repeating_start_idx is not None:
                fractional.insert(repeating_start_idx, '(')
                fractional.append(')')
            result += '.' + ''.join(fractional)

        return result


def tests():
    sol = Solution()
    res = sol.fraction_to_decimal(1, 2)
    print(res)
    res = sol.fraction_to_decimal(2, 1)
    print(res)
    res = sol.fraction_to_decimal(2, 3)
    print(res)
    res = sol.fraction_to_decimal(4, 333)
    print(res)
    res = sol.fraction_to_decimal(1, 5)
    print(res)
    res = sol.fraction_to_decimal(1, 6)
    print(res)
    res = sol.fraction_to_decimal(-50, 8)
    print(res)


tests()
