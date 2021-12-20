"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/822/

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5

Constraints:
-1000 <= a, b <= 1000
"""
from math import log2, ceil


class Solution:
    def get_sum_1(self, a: int, b: int) -> int:
        return round(log2(2**a * 2**b))

    def get_sum_2(self, a: int, b: int) -> int:
        if a >= 0 and b >= 0 or a <= 0 and b <= 0:
            is_negative = a < 0
            while b > 0:
                t = a ^ b
                b = (a & b) << 1
                a = t
            return self.get_sum_2(~a, 1) if is_negative else a
        elif b < 0:
            # b_c = self.get_sum_2(~b, 1)
            # print(f'b_c = {bin(b_c)}')
            return self.get_sum_2(a, b)
        else:
            return self.get_sum_2(b, a)

    def bin_format(self, x):
        num_bytes = ceil(x.bit_length() / 8)  # Number required to represent value.
        ba = x.to_bytes(num_bytes, 'big', signed=x < 0)
        return ''.join('{:08b}'.format(b) for b in ba) + ' ({:4d})'.format(x)

    def get_sum_3(self, a: int, b: int) -> int:
        if a >= 0 and b >= 0 or a <= 0 and b <= 0:
            is_negative = a < 0
            while b > 0:
                t = a ^ b
                b = (a & b) << 1
                a = t
            return self.get_sum_2(~a, 1) if is_negative else a
        elif b < 0:
            # сбросить sign bit для b
            bn = (b & ((1 << b.bit_length()) - 1))
            # сложить как два положительных числа
            res = self.get_sum_2(a, bn)
            print(bin(res))
            # сбросить overflow-бит если есть
            # b_abs = self.get_sum_3(~b, 1)
            # print(b_abs)
            # print(res)
            # if b_abs > a:
            #     return self.get_sum_3(~res, 1)
            return res
        else:
            return self.get_sum_2(b, a)

    def test(self, a: int, b: int):
        for i in range(5):
            t = a ^ b
            print(f'1: {bin(a)} ^ {bin(b)} = {bin(t)} (a)')
            b = (a & b) << 1
            print(f'2: ({bin(a)} & {bin(b)}) << 1 = {bin(b)} (b)')
            a = t
            print('--------------')

        print(a)


def tests():
    sol = Solution()
    # res = sol.get_sum_3(37, 95)
    # print(res)
    # res = sol.get_sum_3(37, 0)
    # print(res)
    # res = sol.get_sum_3(0, 95)
    # print(res)
    # res = sol.get_sum_3(0, 0)
    # print(res)
    # res = sol.get_sum_3(95, -37)
    # print(res)
    # res = sol.get_sum_3(37, -95)
    # print(res)
    # res = sol.get_sum_3(2, -3)
    # print(res)
    # --------------
    # sol.test(95, -37)
    # sol.test(95, 229)
    res = sol.get_sum_3(95, -37)
    print(res)
    res = sol.get_sum_3(37, -95)
    print(res)
    # print(bin(res))
    # print(bin(~(~res & 0xFFFF)))
    # print(~(~res & 0xFFFF))
    # --------------
    # print(sol.bin_format(37))
    # print(sol.bin_format(-37))
    # print(sol.bin_format(-1))
    # print(sol.bin_format(-1 << 7))
    # print(sol.bin_format((-1 << 7) ^ -37))
    # print(int(37).bit_length())


tests()
