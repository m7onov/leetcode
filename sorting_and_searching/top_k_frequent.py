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
        max_freq = 0
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1
            if freqs[n] > max_freq:
                max_freq = freqs[n]

        print(f'k = {k}, freqs = {dict(freqs)}, max_freq = {max_freq}, k / len(nums) = {k / len(nums)}')

        result = []
        for n, f in freqs.items():
            print(f'{n:<2}: f / max_freq = {f / max_freq},    f / len(nums) = {f / len(nums)}')
            if f / max_freq >= k / len(freqs):
                result.append(n)

        return result


def tests():
    sol = Solution()
    # 1, 2
    res = sol.top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    print(res)
    print('-----------')
    # 1
    res = sol.top_k_frequent([1], 1)
    print(res)
    print('-----------')
    # -1, 2
    res = sol.top_k_frequent([4, 1, -1, 2, -1, 2, 3], 2)
    print(res)
    print('-----------')
    # 1, 2
    res = sol.top_k_frequent([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 2)
    print(res)
    print('-----------')
    # 1, 2
    res = sol.top_k_frequent([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 4)
    print(res)
    print('-----------')


tests()

