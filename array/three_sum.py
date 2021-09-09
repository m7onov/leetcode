"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""
from typing import List
from collections import defaultdict


class Solution:
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        np = None
        for i, n in enumerate(nums):
            if n == np:
                continue
            if n > 0:
                break

            np = n
            l = i + 1
            h = len(nums) - 1
            while l < h:
                sm = n + nums[l] + nums[h]
                if sm < 0:
                    l = l + 1
                elif sm > 0:
                    h = h - 1
                else:
                    result.append([n, nums[l], nums[h]])
                    lp = l
                    while l < h and nums[l] == nums[lp]:
                        l = l + 1
                    hp = h
                    while h > l and nums[h] == nums[hp]:
                        h = h - 1

        return result

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        pass


sol = Solution()
print(sol.threeSum1([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum1([-1, -1, 0, 1, -1, 2, -1, -4, 0]))
print(sol.threeSum1([0, 0]))
print(sol.threeSum1([0, 0, 0]))

