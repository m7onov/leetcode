"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/887/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    max_len = None
    min_len = None
    for s in strs:
        if max_len is None or len(s) > max_len:
            max_len = len(s)
        if min_len is None or len(s) < min_len:
            min_len = len(s)

    if min_len is None:
        return ''

    for i in range(min_len):
        cur_char = None
        for s in strs:
            if cur_char is None:
                cur_char = s[i]
            else:
                if s[i] != cur_char:
                    return s[:i]

    return strs[0][:min_len]
