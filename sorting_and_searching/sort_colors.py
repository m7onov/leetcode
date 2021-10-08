"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/798/

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Example 3:
Input: nums = [0]
Output: [0]

Example 4:
Input: nums = [1]
Output: [1]

Constraints:
    | n == nums.length
    | 1 <= n <= 300
    | nums[i] is 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""
from typing import List
"""
The problem is known as Dutch National Flag Problem:
https://en.wikipedia.org/wiki/Dutch_national_flag_problem
"""


class Solution:
    def sort_colors(self, nums: List[int]) -> None:
        a_idx = 0
        z_idx = len(nums) - 1
        idx = a_idx
        while idx <= z_idx:
            if nums[idx] == 0:
                nums[a_idx], nums[idx] = nums[idx], nums[a_idx]
                a_idx += 1
            elif nums[idx] == 2:
                nums[z_idx], nums[idx] = nums[idx], nums[z_idx]
                z_idx -= 1
                # the element at idx position may be zero, so we must try one more time
                # before we increment idx
                continue
            idx += 1


def tests():
    sol = Solution()
    inp = [2, 0, 2, 1, 1, 0]
    sol.sort_colors(inp)
    print(inp)

    inp = [2, 0, 1]
    sol.sort_colors(inp)
    print(inp)

    inp = [0]
    sol.sort_colors(inp)
    print(inp)

    inp = [1]
    sol.sort_colors(inp)
    print(inp)


tests()
