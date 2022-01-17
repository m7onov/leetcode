"""
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/833/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        nums_len = len(nums)
        nums_min = min(nums)
        for i in range(nums_len):
            while (nums[i] - nums_min) < nums_len and nums[i] != i:
                j = nums[i] - nums_min
                nums[j], nums[i] = j, nums[j]

        print(nums)
        return 0


def test():
    sol = Solution()
    res = sol.longest_consecutive([100, 4, 200, 1, 3, 2])
    print(res)


test()
