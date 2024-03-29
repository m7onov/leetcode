"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/810/

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the
order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
from typing import List, Optional
import bisect


class Solution:
    def length_of_lis_0(self, nums: List[int]) -> int:
        nums_len = len(nums)
        lens = [0] * nums_len
        for i in range(nums_len):
            max_len = 0
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    max_len = max(max_len, lens[j])
            lens[i] = max_len + 1
        return max(lens)

    # attempt of slight optimization by storing previous links
    def length_of_lis_1(self, nums: List[int]) -> int:
        pseq = []
        for n in nums:
            idx = bisect.bisect_left(pseq, n)
            if idx < len(pseq):
                pseq[idx] = n
            else:
                pseq.append(n)

        # TODO: find out the real subsequence from pseq
        return len(pseq)


def tests():
    sol = Solution()
    res = sol.length_of_lis_1([10, 9, 2, 5, 3, 7, 101, 18])
    print(res)
    res = sol.length_of_lis_1([1, 50, 100, 20, 21, 22, 23])
    print(res)
    res = sol.length_of_lis_1([0, 1, 0, 3, 2, 3])
    print(res)
    res = sol.length_of_lis_1([1, 3, 6, 7, 9, 4, 10, 5, 6])
    print(res)


tests()
