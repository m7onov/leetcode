"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/4153/

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
    - countAndSay(1) = "1"
    - countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into
        a different digit string.

To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring
contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit.
Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":

.. image:: https://assets.leetcode.com/uploads/2020/10/23/countandsay.jpg

Given a positive integer n, return the n^th term of the count-and-say sequence.

Example 1:
    Input: n = 1
    Output: "1"
    Explanation: This is the base case.

Example 2:
    Input: n = 4
    Output: "1211"
    Explanation:
        countAndSay(1) = "1"
        countAndSay(2) = say "1" = one 1 = "11"
        countAndSay(3) = say "11" = two 1's = "21"
        countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

Constraints:
    1 <= n <= 30
"""


class Solution:
    def count_and_say(self, n: int) -> str:
        s1 = [1]
        s2 = []
        for _ in range(n - 1):
            n = s1[0]
            c = 1
            for x in s1[1:]:
                if x == n:
                    c += 1
                else:
                    s2.append(c)
                    s2.append(n)
                    n = x
                    c = 1
            s2.append(c)
            s2.append(n)
            s1 = s2
            s2 = []

        return "".join(str(x) for x in s1)


def test1():
    sol = Solution()
    for i in range(1, 11):
        res = sol.count_and_say(i)
        print(f"{i}: {res}")


test1()
