"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/824/

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 10^4
-2^31 <= nums[i] <= 2^31 - 1

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List
# for testing
from random import shuffle, randint


# noinspection PyMethodMayBeStatic
class Solution:
    def majority_element(self, nums: List[int]) -> int:
        # O(n*log(n)) - cpu, O(n) - memory
        nums_sorted = sorted(nums)
        return nums_sorted[len(nums_sorted) // 2]

    def majority_element_2(self, nums: List[int]) -> int:
        # O(?) - cpu, O(1) - memory
        def partition(start_idx, stop_idx, pivot_idx) -> int:
            nums[stop_idx], nums[pivot_idx] = nums[pivot_idx], nums[stop_idx]
            store_idx = start_idx
            for i in range(start_idx, stop_idx):
                if nums[i] <= nums[stop_idx]:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1

            nums[store_idx], nums[stop_idx] = nums[stop_idx], nums[store_idx]
            return store_idx

        def quickselect(start_idx, stop_idx, req_idx):
            pivot_idx = randint(start_idx, stop_idx)
            pivot_true_idx = partition(start_idx, stop_idx, pivot_idx)
            print(f'[{start_idx, stop_idx}], pivot_idx = {pivot_idx}, pivot_true_idx = {pivot_true_idx}')

            pivot_val = nums[pivot_true_idx]
            for i in range(pivot_true_idx - 1, start_idx - 1, -1):
                if pivot_true_idx == req_idx:
                    return
                elif nums[i] == pivot_val:
                    pivot_true_idx -= 1
                else:
                    break

            if pivot_true_idx < req_idx:
                quickselect(pivot_true_idx + 1, stop_idx, req_idx)
            elif pivot_true_idx > req_idx:
                quickselect(start_idx, pivot_true_idx - 1, req_idx)

        quickselect(0, len(nums) - 1, len(nums) // 2)
        return nums[len(nums) // 2]

    def majority_element_3(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        candidate = None
        counter = 0
        for n in nums:
            if candidate is None:
                candidate = n

            if n == candidate:
                counter += 1
            else:
                counter -= 1

            if counter == 0:
                candidate = None

        return candidate


def tests():
    sol = Solution()

    res = sol.majority_element_3([3, 2, 3])
    print(f'{res} == 3')

    res = sol.majority_element_3([2, 2, 1, 1, 1, 2, 2])
    print(f'{res} == 2')

    a = [5 for _ in range(20)]
    b = [randint(1, 30) for _ in range(19)]
    c = a + b
    shuffle(c)
    res = sol.majority_element_3(c)
    print(f'{res} == 5')

    a = [5 for _ in range(25001)]
    b = [randint(1, 500) for _ in range(24999)]
    c = a + b
    shuffle(c)
    res = sol.majority_element_3(c)
    print(f'{res} == 5')

    a = [5 for _ in range(50000)]
    res = sol.majority_element_3(a)
    print(f'{res} == 5')


tests()