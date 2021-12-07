"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/817/

Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding
column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701

Example 4:
Input: columnTitle = "FXSHRXW"
Output: 2147483647

Constraints:
1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""


class Solution:
    def title_to_number(self, column_title: str) -> int:
        num = 0
        ctl = len(column_title)
        for i, c in enumerate(column_title):
            cn = ord(c) - 64
            num += cn * (26**(ctl - i - 1))
        return num


def tests():
    sol = Solution()
    res = sol.title_to_number('A')
    print(res)
    res = sol.title_to_number('AB')
    print(res)
    res = sol.title_to_number('ZY')
    print(res)
    res = sol.title_to_number('FXSHRXW')
    print(res)


tests()
