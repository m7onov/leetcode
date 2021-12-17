"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/823/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
Note that division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a
result, and there will not be any division by zero operation.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:
1 <= tokens.length <= 10^4
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""
from typing import List


class Solution:
    def eval_rpn(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}
        queue = []
        for t in tokens:
            print(f'queue before: {queue}')
            if t not in ops:
                queue.append(t)
            else:
                b = queue.pop()
                a = queue.pop()
                if t == '+':
                    c = int(a) + int(b)
                elif t == '-':
                    c = int(a) - int(b)
                elif t == '*':
                    c = int(a) * int(b)
                elif t == '/':
                    is_negative = int(a) < 0 < int(b) or int(b) < 0 < int(a)
                    c = abs(int(a)) // abs(int(b))
                    c *= -1 if is_negative else 1
                else:
                    raise Exception(f'unknown operator: {t}')

                print(f'queue append result: {a} {t} {b} = {c}')
                queue.append(str(c))

        return int(queue[-0])


def tests():
    sol = Solution()
    res = sol.eval_rpn(['2', '1', '+', '3', '*'])
    print(res)
    res = sol.eval_rpn(['4', '13', '5', '/', '+'])
    print(res)
    res = sol.eval_rpn(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'])
    print(res)


tests()
