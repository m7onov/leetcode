"""
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/836/

Given a string s which represents an expression, evaluate this expression and return its value.
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the
range of [-2^31, 2^31 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5

Constraints:
    - 1 <= s.length <= 3 * 10^5
    - s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
    - s represents a valid expression.
    - All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
    - The answer is guaranteed to fit in a 32-bit integer.
"""
from typing import Set


class Solution:
    def calculate1(self, s: str) -> int:
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

        def apply_op(larg, rarg, op):
            if op == '*':
                return [str(int(''.join(larg)) * int(''.join(rarg)))]
            elif op == '/':
                return [str(int(''.join(larg)) // int(''.join(rarg)))]
            elif op == '+':
                return [str(int(''.join(larg)) + int(''.join(rarg)))]
            elif op == '-':
                return [str(int(''.join(larg)) - int(''.join(rarg)))]

        def collapse_eq_prec_ops(inp: str, op_names: Set[str]) -> str:
            ret_str = []
            op = None
            larg = []
            rarg = []
            for i, c in enumerate(x for x in inp if x != ' '):
                if op is None:
                    if c in digits:
                        larg.append(c)
                    elif c in op_names:
                        op = c
                    else:
                        ret_str += larg
                        ret_str.append(c)
                        larg.clear()
                else:
                    if c in digits:
                        rarg.append(c)
                    elif c in op_names:
                        larg = apply_op(larg, rarg, op)
                        rarg.clear()
                        op = c
                    else:
                        larg = apply_op(larg, rarg, op)
                        ret_str += larg
                        ret_str.append(c)
                        larg.clear()
                        rarg.clear()
                        op = None
            else:
                if op is not None:
                    larg = apply_op(larg, rarg, op)
                    rarg.clear()

            ret_str += larg
            return ''.join(ret_str)

        s = collapse_eq_prec_ops(s, {'*', '/'})
        s = collapse_eq_prec_ops(s, {'+', '-'})
        return int(''.join(s))

    def calculate2(self, s: str) -> int:
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        ret, sign,  larg, rarg, op = 0, 1, 0, 0, None
        for i, c in enumerate(x for x in s if x != ' '):
            if op is not None:
                if c in digits:
                    rarg = 10 * rarg + int(c)
                    continue
                else:
                    larg = ((larg * rarg) if op == '*' else (larg // rarg))
                    op = None
                    rarg = 0
            if c in {'+', '-'}:
                ret += sign * larg
                sign = 1 if c == '+' else -1
                larg = 0
            elif c in {'*', '/'}:
                op = c
            else:
                larg = 10 * larg + int(c)
        else:
            if op is not None:
                larg = ((larg * rarg) if op == '*' else (larg // rarg))
            ret += sign * larg
        return ret


def tests():
    sol = Solution()
    for s, ans in [('0-123', -123), ('1*2+3*4', 14), ('1+1+1', 3), (' 3+5 / 2', 5), (' 3/2 ', 1), ('3+2*2', 7)]:
        res = sol.calculate2(s)
        print(f'{s} -> {res} == {ans}')


tests()
