"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/885/

Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr()
and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0
"""


def str_str(haystack: str, needle: str) -> int:
    if needle == '':
        return 0

    ln = len(needle)
    lh = len(haystack)

    if ln > lh:
        return -1

    for i, c in enumerate(haystack):
        if lh - i < ln:
            return -1

        for j in range(ln):
            if haystack[i + j] == needle[j]:
                continue
            else:
                break
        else:
            return i

    return -1

# TODO: Rabin Karp algorithm using rolling hash
