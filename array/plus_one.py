"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/559/

Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array
contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
"""
from typing import List


def plus_one(digits: List[int]) -> List[int]:
    overflow = 1
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] + overflow == 10:
            digits[i] = 0
        else:
            digits[i] += overflow
            overflow = 0
            break

    if overflow:
        digits.insert(0, 1)

    return digits
