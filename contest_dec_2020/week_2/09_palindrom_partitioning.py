"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3565/

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome
partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
"""
from typing import List
from collections import defaultdict
import profile


class MySolution:
    def __init__(self):
        self.partitions = []
        self.palindroms = []
        self.s = ''
        self.sln = len(self.s)

    def get_palindroms(self):
        palindroms = defaultdict(list)
        for i in range(self.sln):
            k = min(self.sln - i, i + 1)
            for j in range(k):
                left_side = self.s[i-j:i]
                right_side = self.s[i+1:i+1+j]
                if left_side == right_side[::-1]:
                    palindroms[i-j].append((i-j, i+1+j))

                if j >= 0 and i+2+j <= self.sln:
                    left_side = self.s[i-j:i+1]
                    right_side = self.s[i+1:i+2+j]
                    if left_side == right_side[::-1]:
                        palindroms[i-j].append((i-j, i+2+j))

        return palindroms

    def get_partitions_recursive(self, start_idx: int, partition: List[str]):
        if start_idx >= self.sln:
            self.partitions.append(partition)
            return

        for li, ri in self.palindroms[start_idx]:
            self.get_partitions_recursive(start_idx+ri-li,
                                          partition + [self.s[start_idx:start_idx+ri-li]])

    def partition(self, s: str) -> List[List[str]]:
        # NOTE: решение основано на том, что сначала мы генерируем все палиндромы-подстроки (start_idx, stop_idx),
        #       а потом генерируем все допустимые комбинации палиндромов рекурсивно
        self.s = s
        self.sln = len(s)
        self.palindroms = self.get_palindroms()
        self.get_partitions_recursive(0, [])
        return self.partitions


sol = MySolution()
profile.run('''sol.partition('aaaaaaaaaaaaaaaa')''')


# более простое решение (чужое)
# class Solution2:
#     def isPal(self, s):
#         return s == s[::-1]
#
#     def dfs(self, s, path, res):
#         if not s:
#             res.append(path)
#             return
#         for i in range(1, len(s) + 1):
#             if self.isPal(s[:i]):
#                 self.dfs(s[i:], path + [s[:i]], res)
#
#     def partition(self, s):
#         res = []
#         self.dfs(s, [], res)
#         return res
#
#
# sol2 = Solution2()
# profile.run('''sol2.partition('aaaaaaaaaaaaaaaa')''')


# более просто решение (чужое)
# class Solution3:
#     def partition(self, s: str) -> List[List[str]]:
#         if not s:
#             return []
#
#         dp = {0: [[]], 1: [[s[0]]]}
#
#         for i in range(1, len(s)):
#             dp[i + 1] = []
#
#             for j in range(0, i + 1):
#                 if self.is_palindrome(s[j:i + 1]):
#                     for prev in dp[j]:
#                         dp[i + 1].append(prev + [s[j:i + 1]])
#
#         return dp[len(s)]
#
#     def is_palindrome(self, s):
#         return s == s[::-1]


# sol3 = Solution3()
# profile.run('''sol3.partition('abba')''')
