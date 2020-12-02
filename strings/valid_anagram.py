"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/882/

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the strings contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    dc = [0] * 26
    start_ord = ord('a')

    for c in s:
        dc[ord(c) - start_ord] += 1

    for c in t:
        i = ord(c) - start_ord
        dc[i] -= 1
        if dc[i] < 0:
            return False

    for c in dc:
        if c != 0:
            return False

    return True
