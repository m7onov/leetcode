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
import random


class Solution:
    def first_missing_positive1(self, nums: List[int]) -> int:
        nums_len = len(nums)
        for i in range(nums_len):
            while nums[i] != 0 and nums[i] != i + 1:
                j = nums[i] - 1
                if 0 <= j < nums_len and nums[j] != nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                else:
                    nums[i] = 0

        for i, n in enumerate(nums):
            if n == 0:
                return i + 1

        return nums_len + 1

    def first_missing_positive2(self, nums: List[int]) -> int:
        nums_len = len(nums)

        if 1 not in nums:
            return 1

        for i, n in enumerate(nums):
            if n <= 0 or n > nums_len:
                nums[i] = 1

        for i, n in enumerate(nums):
            j = abs(n) - 1
            nums[j] = -abs(nums[j])

        for i, n in enumerate(nums):
            if n > 0:
                return i + 1

        return nums_len + 1


def test():
    sol = Solution()
    res = sol.first_missing_positive2([1, 2, 0])
    print(f'3 = {res}')
    res = sol.first_missing_positive2([3, 4, -1, 1])
    print(f'2 = {res}')
    res = sol.first_missing_positive2([7, 8, 9, 11, 12])
    print(f'1 = {res}')
    res = sol.first_missing_positive2([2, 1])
    print(f'3 = {res}')
    res = sol.first_missing_positive2([-7, 1, 8, -5, 2, 7, -10, 3, 6])
    print(f'4 = {res}')
    res = sol.first_missing_positive2([1, 1, 1, 1, 1])
    print(f'2 = {res}')


def random_tests():
    sol = Solution()
    arr = [i for i in range(-99, 100)]
    for i in range(30):
        arr.pop(random.randint(-99, 99))

    ans = None
    prev = 0
    for i in sorted(arr):
        if i > 0:
            if i != prev + 1:
                ans = prev + 1
                break
            else:
                prev += 1

    res = sol.first_missing_positive2(arr)
    print(f'{ans == res}')


test()
for _ in range(100):
    random_tests()
