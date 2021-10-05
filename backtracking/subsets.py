"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def recurse(from_idx):
            if from_idx == len(nums):
                result.append([])
                return
            recurse(from_idx + 1)
            for i in range(len(result)):
                result.append([nums[from_idx]] + result[i])

        recurse(0)
        return result


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for n in nums:
            for i in range(len(result)):
                result.append(result[i] + [n])
        return result


class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        output = []

        def backtrack(from_idx):
            result.append(output.copy())
            for i in range(from_idx, len(nums)):
                output.append(nums[i])
                backtrack(i + 1)
                output.pop()

        backtrack(0)
        return result


class Solution4:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(2**len(nums), 2**(len(nums) + 1)):
            result.append([nums[j] for j, c in enumerate(bin(i)[3:]) if c == '1'])
        return result


def tests():
    sol = Solution4()
    res = sol.subsets([1, 2, 3])
    print(res)


tests()

