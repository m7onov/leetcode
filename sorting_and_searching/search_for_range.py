"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/802/

Given an array of integers nums sorted in ascending order, find the starting and ending position
of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
"""
from typing import List


class Solution:
    def search_range(self, nums: List[int], target: int) -> List[int]:
        def binary_search_border(start_idx, stop_idx, direction):
            if start_idx == stop_idx:
                return start_idx
            middle_idx = (start_idx + stop_idx) // 2 + (1 if direction == 'right' else 0)
            if nums[middle_idx] != target:
                if direction == 'left':
                    return binary_search_border(middle_idx + 1, stop_idx, direction)
                else:
                    return binary_search_border(start_idx, middle_idx - 1, direction)
            else:
                if direction == 'left':
                    return binary_search_border(start_idx, middle_idx, direction)
                else:
                    return binary_search_border(middle_idx, stop_idx, direction)

        def binary_search(start_idx, stop_idx):
            if start_idx == stop_idx and nums[start_idx] != target:
                return [-1, -1]

            middle_idx = (start_idx + stop_idx) // 2
            if nums[middle_idx] < target:
                return binary_search(middle_idx + 1, stop_idx)
            elif nums[middle_idx] > target:
                return binary_search(start_idx, middle_idx)
            else:
                left_idx = binary_search_border(start_idx, middle_idx, 'left')
                right_idx = binary_search_border(middle_idx, stop_idx, 'right')
                return [left_idx, right_idx]

        if len(nums) == 0:
            return [-1, -1]
        else:
            return binary_search(0, len(nums) - 1)


def tests():
    sol = Solution()
    res = sol.search_range([5, 7, 7, 8, 8, 10], 8)
    print(f'{res} == [3, 4]')
    res = sol.search_range([5, 7, 7, 6, 8, 8, 10], 10)
    print(f'{res} == [6, 6]')
    res = sol.search_range([5, 7, 7, 8, 8, 10], 6)
    print(f'{res} == [-1, -1]')
    res = sol.search_range([], 0)
    print(f'{res} == [-1, -1]')
    res = sol.search_range([2, 2], 2)
    print(f'{res} == [0, 1]')
    res = sol.search_range([2, 2], 1)
    print(f'{res} == [-1, -1]')
    res = sol.search_range([5, 6, 7, 8, 8, 10], 7)
    print(f'{res} == [2, 2]')


tests()
