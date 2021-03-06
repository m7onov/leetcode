"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

Given a sorted array nums, remove the duplicates in-place such that each element
appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input
array in-place with O(1) extra memory.
"""
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            i += 1

    return len(nums)
