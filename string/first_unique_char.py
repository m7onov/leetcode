"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/881/

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.
s = "loveleetcode"
return 2.

Note: You may assume the string contains only lowercase English letters.
"""


def first_uniq_char(s: str) -> int:
    dc = {}
    for i, c in enumerate(s):
        if c in dc:
            dc[c] = -1
        else:
            dc[c] = i

    for c, i in dc.items():
        if i >= 0:
            return i

    return -1
