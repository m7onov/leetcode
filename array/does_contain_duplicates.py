"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if
every element is distinct.
"""
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    if len(nums) < 2:
        return False

    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True

    return False
