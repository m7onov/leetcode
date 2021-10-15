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
from collections import defaultdict
import heapq
import random


class SolutionBruteForce:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1
        result = [i[0] for i in sorted(freqs.items(), key=lambda x: x[1], reverse=True)]
        return result[:k]


class SolutionMaxHeap:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1
        result = heapq.nlargest(k, freqs.items(), key=lambda x: x[1])
        result = [i[0] for i in result]
        return result


class SolutionQuickSelect:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1

        keys = [f for f in freqs.keys()]
        ln = len(keys)

        def partition(start_idx, stop_idx, pivot_idx):
            keys[stop_idx], keys[pivot_idx] = keys[pivot_idx], keys[stop_idx]
            store_idx = start_idx
            for i in range(start_idx, stop_idx):
                if freqs[keys[i]] < freqs[keys[stop_idx]]:
                    keys[i], keys[store_idx] = keys[store_idx], keys[i]
                    store_idx += 1

            keys[stop_idx], keys[store_idx] = keys[store_idx], keys[stop_idx]
            return store_idx

        def quickselect(start_idx, stop_idx, req_len):
            pivot_idx = random.randint(start_idx, stop_idx)
            pivot_true_idx = partition(start_idx, stop_idx, pivot_idx)
            if pivot_true_idx == req_len:
                return
            elif pivot_true_idx < req_len:
                quickselect(pivot_true_idx, stop_idx, req_len)
            else:
                quickselect(start_idx, pivot_true_idx, req_len)

        quickselect(0, ln - 1, ln - k)
        return keys[ln-k:]


def tests():
    sol = SolutionQuickSelect()
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
    # 1, 2, 3, 4
    res = sol.top_k_frequent([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 4)
    print(res)
    print('-----------')


tests()

