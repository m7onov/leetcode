"""
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/832/

Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

Constraints:
1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""
from typing import List


class Solution:
    def first_missing_positive(self, nums: List[int]) -> int:
        min_val = float('inf')
        max_val = float('-inf')
        counter = 0
        for n in nums:
            if n > 0:
                if n < min_val:
                    min_val = n
                if n > max_val:
                    max_val = n
                counter += 1

        print(f'min_val = {min_val}, max_val = {max_val}, counter = {counter}')
        if counter < max_val - min_val:
            pass

        return 0


def test():
    sol = Solution()
    # res = sol.first_missing_positive([1, 2, 0])
    # print(res)
    # res = sol.first_missing_positive([3, 4, -1, 1])
    # print(res)
    # res = sol.first_missing_positive([7, 8, 9, 11, 12])
    # print(res)
    res = sol.first_missing_positive([2, 1])
    print(res)


test()
