"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/879/

Write a function that reverses a strings. The input strings is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra
memory.
You may assume all the characters consist of printable ascii characters.

Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List


def reverse_string(s: List[str]) -> None:
    n = len(s)
    for i in range(n // 2):
        s[i], s[n-i-1] = s[n-i-1], s[i]

