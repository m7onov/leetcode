"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/721/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pars = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in pars.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or pars[stack[-1]] != c:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0


sol = Solution()
print(sol.isValid('()'))
print(sol.isValid('()[]{}'))
print(sol.isValid('(]'))
print(sol.isValid('([)]'))
print(sol.isValid('{[]}'))


print(sol.isValid('{{}[][[[]]]}'))