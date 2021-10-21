"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/804/

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        def bin_search(from_idx, to_idx) -> int:
            while to_idx > from_idx:
                mid_idx = (from_idx + to_idx) // 2
                if nums[mid_idx] > target:
                    to_idx = mid_idx
                elif nums[mid_idx] < target:
                    from_idx = mid_idx + 1
                else:
                    return mid_idx
            return from_idx if nums[from_idx] == target else -1

        start_idx = 0
        stop_idx = len(nums) - 1
        while stop_idx >= start_idx:
            middle_idx = (start_idx + stop_idx) // 2
            if nums[middle_idx] == target:
                return middle_idx

            if nums[middle_idx] < nums[start_idx]:
                stop_idx = middle_idx
            elif nums[middle_idx] > nums[stop_idx]:
                start_idx = middle_idx + 1
            else:
                break

        res = bin_search(0, start_idx - 1)
        return res if res != -1 else bin_search(start_idx, len(nums) - 1)


class SolutionOnePass():
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        start_idx = 0
        end_idx = len(nums) - 1
        while start_idx < end_idx:
            middle_idx = (start_idx + end_idx) // 2

            if nums[middle_idx] == target:
                return middle_idx

            if nums[middle_idx] >= nums[start_idx]:
                if nums[start_idx] <= target <= nums[middle_idx]:
                    end_idx = middle_idx
                else:
                    start_idx = middle_idx + 1
            else:
                if nums[middle_idx] < target <= nums[end_idx]:
                    start_idx = middle_idx + 1
                else:
                    end_idx = middle_idx

        return start_idx if nums[start_idx] == target else -1


def tests():
    sol = SolutionOnePass()
    res = sol.search([1, 2, 3, 4, 5, 6, 7, 8], 8)
    print(7 == res)
    res = sol.search([6, 7, 8, 1, 2, 3, 4, 5], 8)
    print(2 == res)
    res = sol.search([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 0)
    print(9 == res)
    res = sol.search([1, 2], 1)
    print(0 == res)
    res = sol.search([2, 1], 1)
    print(1 == res)
    res = sol.search([2, 1], 3)
    print(-1 == res)
    res = sol.search([2, 3, 4, 1], 2)
    print(0 == res)
    res = sol.search([1], 1)
    print(0 == res)
    res = sol.search([1], 2)
    print(-1 == res)
    res = sol.search([], 2)
    print(-1 == res)


tests()