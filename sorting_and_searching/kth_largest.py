"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/800/

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 104
-10^4 <= nums[i] <= 10^4
"""
import random
from typing import List
from collections import defaultdict


class Solution:
    def find_kth_largest_quicksort(self, nums: List[int], k: int) -> int:
        def partition(start_idx, stop_idx, pivot_idx):
            nums[pivot_idx], nums[stop_idx] = nums[stop_idx], nums[pivot_idx]
            store_idx = start_idx
            for i in range(start_idx, stop_idx):
                if nums[i] < nums[stop_idx]:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1

            nums[store_idx], nums[stop_idx] = nums[stop_idx], nums[store_idx]
            return store_idx

        def quicksort(start_idx, stop_idx):
            if stop_idx <= start_idx:
                return
            pivot_idx = random.randint(start_idx, stop_idx)
            pivot_true_idx = partition(start_idx, stop_idx, pivot_idx)
            quicksort(start_idx, pivot_true_idx - 1)
            quicksort(pivot_true_idx + 1, stop_idx)

        quicksort(0, len(nums) - 1)
        return nums[-k]

    def find_kth_largest_quickselect(self, nums: List[int], k: int) -> int:
        def partition(start_idx, stop_idx, pivot_idx):
            nums[pivot_idx], nums[stop_idx] = nums[stop_idx], nums[pivot_idx]
            store_idx = start_idx
            for i in range(start_idx, stop_idx):
                if nums[i] < nums[stop_idx]:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1

            nums[store_idx], nums[stop_idx] = nums[stop_idx], nums[store_idx]
            return store_idx

        def quicksort(start_idx, stop_idx, req_idx):
            pivot_idx = random.randint(start_idx, stop_idx)
            pivot_true_idx = partition(start_idx, stop_idx, pivot_idx)

            for i in range(pivot_true_idx, stop_idx + 1):
                if nums[i] != nums[pivot_true_idx]:
                    break
                elif i == req_idx:
                    return

            print(f'start_idx = {start_idx}, stop_idx = {stop_idx}, pivot_idx = {pivot_idx}, pivot_true_idx = {pivot_true_idx}, req_idx = {req_idx}, nums = {nums}')
            if pivot_true_idx < req_idx:
                quicksort(pivot_true_idx, stop_idx, req_idx)
            elif pivot_true_idx > req_idx:
                quicksort(start_idx, pivot_true_idx, req_idx)

        quicksort(0, len(nums) - 1, len(nums) - k)
        return nums[-k]


def tests():
    sol = Solution()
    res = sol.find_kth_largest_quickselect([3, 2, 1, 5, 6, 4], 2)
    print(res)
    res = sol.find_kth_largest_quickselect([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    print(res)
    res = sol.find_kth_largest_quickselect([99, 99], 1)
    print(res)
    res = sol.find_kth_largest_quickselect([-1, -1], 2)
    print(res)


tests()
