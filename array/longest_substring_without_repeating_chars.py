"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""
from collections import defaultdict


class Solution:
    # O(L) - speed
    # O(1) - memory (string chars dictionary is limited anyway)
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = dict()
        max_len = 0
        start_pos = 0
        end_pos = None
        for end_pos, c in enumerate(s):
            if c in m and m[c] >= start_pos:
                max_len = max(max_len, end_pos - start_pos)
                start_pos = m[c] + 1
            m[c] = end_pos
            # print(m)
            # print(start_pos, end_pos)
            # print('------------------------')
        else:
            # print(m)
            # print(start_pos, end_pos)
            if end_pos is not None:
                end_pos += 1
            else:
                end_pos = 0

        max_len = max(max_len, end_pos - start_pos)
        return max_len


sol = Solution()
res = sol.lengthOfLongestSubstring('abcabcbb')
print(res)
res = sol.lengthOfLongestSubstring('bbbbb')
print(res)
res = sol.lengthOfLongestSubstring('pwwkew')
print(res)
res = sol.lengthOfLongestSubstring('')
print(res)
res = sol.lengthOfLongestSubstring(' ')
print(res)
res = sol.lengthOfLongestSubstring('dvdf')
print(res)
res = sol.lengthOfLongestSubstring('abba')
print(res)
