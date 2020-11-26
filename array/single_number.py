"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/549/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
"""
from typing import List


def single_number(nums: List[int]) -> int:
    return 2 * sum(set(nums)) - sum(nums)
