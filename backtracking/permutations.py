"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/795/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
    * 1 <= nums.length <= 6
    * -10 <= nums[i] <= 10
    * All the integers of nums are unique.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        result = []
        for i in range(len(nums)):
            v = nums.pop(i)
            for p in self.permute(nums):
                result.append([v] + p)
            nums.insert(i, v)

        return result


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(from_idx):
            if from_idx == len(nums) - 1:
                return result.append(nums.copy())
            for i in range(from_idx, len(nums)):
                nums[from_idx], nums[i] = nums[i], nums[from_idx]
                backtrack(from_idx + 1)
                nums[from_idx], nums[i] = nums[i], nums[from_idx]

        backtrack(0)
        return result


def tests():
    sol = Solution2()
    res = sol.permute([1, 2, 3])
    print(res)
    res = sol.permute([0, 1])
    print(res)
    res = sol.permute([1])
    print(res)
    res = sol.permute([1, 2, 3, 4])
    print(res)


tests()
