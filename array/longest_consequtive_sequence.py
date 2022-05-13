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
        m = set(nums)  # O(n)
        max_len = 0

        # В сумме 3 while дадут ровно n итераций => O(n)
        while len(m) > 0:
            n = m.pop()
            ln = 1

            i = 1
            while n + i in m:
                m.discard(n + i)
                ln += 1
                i += 1

            i = 1
            while n - i in m:
                m.discard(n - i)
                ln += 1
                i += 1

            max_len = max(ln, max_len)

        return max_len


def test():
    sol = Solution()
    res = sol.longest_consecutive([100, 4, 200, 1, 3, 2])
    print(res)
    res = sol.longest_consecutive([100, 4, 200, 1, 3, 2, 201, 202, 203, 204])
    print(res)


test()
