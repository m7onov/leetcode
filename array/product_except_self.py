"""
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/827/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space
for space complexity analysis.)
"""
from typing import List


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        ret_list = nums.copy()
        for i in range(len(nums) - 2, -1, -1):
            ret_list[i] *= ret_list[i + 1]

        rolling_product = 1
        for i in range(len(nums) - 1):
            tmp = nums[i]
            ret_list[i] = ret_list[i + 1] * rolling_product
            rolling_product *= tmp

        ret_list[-1] = rolling_product
        return ret_list


def test():
    sol = Solution()
    res = sol.product_except_self([1, 2, 3, 4])
    print(res)
    res = sol.product_except_self([-1, 1, 0, -3, 3])
    print(res)


test()
