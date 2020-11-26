"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/646/

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
from typing import List


def rotate(nums: List[int], k: int) -> None:
    if len(nums) < 2:
        return

    for i in range(k):
        e = nums.pop(-1)
        nums.insert(0, e)
