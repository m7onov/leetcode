"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/794/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8
"""
from typing import List
from collections import deque


"""
Заметки:
https://ru.wikipedia.org/wiki/Правильная_скобочная_последовательность

Правильные скобочные последовательности образуют язык Дика и формально определяются следующим образом:
    - пустая строка — правильная скобочная последовательность;
    - правильная скобочная последовательность, взятая в скобки одного типа — правильная скобочная последовательность;
    - правильная скобочная последовательность, к которой приписана слева или справа правильная скобочная 
      последовательность тоже правильная скобочная последовательность.
"""


class SolutionWrong1:
    def __init__(self):
        self.num_pairs = 0
        self.result = set()
        self.combination = deque()

    def dive(self, pair_idx, left_part, right_part):
        for c in reversed(left_part):
            self.combination.appendleft(c)
        for c in right_part:
            self.combination.append(c)
        self.recursion(pair_idx)
        for _ in range(len(left_part)):
            self.combination.popleft()
        for _ in range(len(right_part)):
            self.combination.pop()

    def recursion(self, pair_idx: int):
        if pair_idx == 0:
            self.dive(pair_idx + 1, [], ['(', ')'])
        elif pair_idx < self.num_pairs:
            self.dive(pair_idx + 1, ['(', ')'], [])
            self.dive(pair_idx + 1, [], ['(', ')'])
            self.dive(pair_idx + 1, ['('], [')'])
        else:
            self.result.add(''.join(self.combination))

    def generate_parenthesis(self, n: int) -> List[str]:
        self.num_pairs = n
        self.recursion(0)
        return [c for c in self.result]


class SolutionBruteForce:
    def check(self, comb):
        srepr = []
        counter = 0
        for i in comb:
            if i == '0':
                srepr.append(')')
                counter -= 1
            else:
                srepr.append('(')
                counter += 1
            if counter < 0:
                return None

        if counter == 0:
            return ''.join(srepr)
        else:
            return None

    def generate_parenthesis(self, n: int) -> List[str]:
        result = set()
        for i in range(2**(2*n-1), 2**(2*n)-1):
            b = bin(i)[2:]
            c = self.check(b)
            if c is not None:
                result.add(c)
        return [r for r in result]


class SolutionRecursive1:
    def generate_parenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        elif n == 1:
            return ['()']
        else:
            result = []
            for i in range(n):
                for j in self.generate_parenthesis(i):
                    for k in self.generate_parenthesis(n - i - 1):
                        result.append('(' + j + ')' + k)
            return result


def tests():
    sol = SolutionRecursive1()
    print(len(sol.generate_parenthesis(6)))


tests()
