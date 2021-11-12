"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/807/

You are given an integer array nums. You are initially positioned at the array's first index, and each element in
the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible
to reach the last index.

Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def can_jump_1(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        if nums_len == 1:
            return True

        max_i = 0
        for i in range(nums_len - 1):
            max_i = max(max_i, i + nums[i])
            if max_i >= nums_len - 1:
                return True
            if max_i <= i:
                return False

        return False

    def can_jump_2(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        end_idx = nums_len - 1
        memo_table = ['U'] * nums_len
        memo_table[-1] = 'G'
        for i in range(end_idx - 1, -1, -1):
            if memo_table[i] == 'U':
                for j in range(i + 1, min(i + 1 + nums[i], nums_len)):
                    if memo_table[j] == 'G':
                        memo_table[i] = 'G'
                        break
                else:
                    memo_table[i] = 'B'

        print(f'memo_table = {memo_table}')
        return memo_table[0] == 'G'


def tests():
    sol = Solution()
    res = sol.can_jump_2([2, 3, 1, 1, 4])
    print(res)
    res = sol.can_jump_2([3, 2, 1, 0, 4])
    print(res)


tests()
