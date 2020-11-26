"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/567/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
from typing import List


def move_zeroes(nums: List[int]) -> None:
    num_moved = 0
    for i in range(len(nums)):
        if nums[i - num_moved] == 0:
            nums.pop(i - num_moved)
            nums.append(0)
            num_moved += 1
