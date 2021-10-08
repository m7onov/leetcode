"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any
order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from typing import List
from collections import defaultdict, deque


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1

        for n, f in freqs.items():
            pass

        return []
        # top_freqs = deque()
        # for n, f in freqs.items():
        #     if len(top_freqs) < k:
        #         if f > top_freqs[0][1]:
        #             top_freqs.appendleft((n, f))
        #     if len(top_freqs) > k:
        #         top_freqs.pop()
        #
        # return [n for n, f in top_freqs]


def tests():
    sol = Solution()
    # res = sol.top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    # print(res)
    #
    # res = sol.top_k_frequent([1], 1)
    # print(res)

    res = sol.top_k_frequent([4, 1, -1, 2, -1, 2, 3], 2)
    print(res)


tests()
