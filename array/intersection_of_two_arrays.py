"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/674/

Given two arrays, write a function to compute their intersection.

Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the
memory at once?
"""
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_counters = {}
    nums2_counters = {}

    for n in nums1:
        nums1_counters[n] = nums1_counters.get(n, 0) + 1

    for n in nums2:
        nums2_counters[n] = nums2_counters.get(n, 0) + 1

    ret_list = []
    for n in nums1_counters.keys():
        if n in nums2_counters:
            ret_list.extend(min(nums1_counters[n], nums2_counters[n]) * [n])

    return ret_list
