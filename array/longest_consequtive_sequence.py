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
import random


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

    def longest_consecutive2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cache1 = dict()
        for n in nums:
            if n not in cache1:
                print('---------------------')
                print(f'n = {n}')
                cache1[n] = 1
                right_border = n + cache1[n]
                print(f'(A) cache = {cache1}')
                print(f'(A) right_border = {right_border}, {right_border in cache1}')
                while right_border in cache1:
                    cache1[n] += cache1[right_border]
                    cache1.pop(right_border)
                    right_border = n + cache1[n]
                    print(f'(A) cache = {cache1}')
                    print(f'(A) right_border = {right_border}, {right_border in cache1}')

        print('\n')
        for n in list(cache1.keys()):
            if n in cache1:
                print(f'n = {n}')
                right_border = n + cache1[n]
                print(f'(B) cache = {cache1}')
                print(f'(B) right_border = {right_border}, {right_border in cache1}')
                while right_border in cache1:
                    cache1[n] += cache1[right_border]
                    cache1.pop(right_border)
                    right_border = n + cache1[n]
                    print(f'(B) cache = {cache1}')
                    print(f'(B) right_border = {right_border}, {right_border in cache1}')

        print(cache1)
        return max(cache1.values())


def test():
    sol = Solution()
    # res = sol.longest_consecutive2([100, 4, 200, 1, 3, 2])
    res = sol.longest_consecutive2([7, -9, 3, -6, 3, 5, 3, 6, -2, -5, 8, 6, -4, -6, -4, -4, 5, -9, 2, 7, 0, 0])
    print(res)


def random_test():
    sol = Solution()
    inp = [random.randint(1, 100) for _ in range(100)]
    inp = [7, -9, 3, -6, 3, 5, 3, 6, -2, -5, 8, 6, -4, -6, -4, -4, 5, -9, 2, 7, 0, 0]
    print(f'inp = {inp}')
    inp_sorted = sorted(inp)
    print(f'inp_sorted = {inp_sorted}')
    ans = 0
    seq = 0
    prev = None
    for n in inp_sorted:
        if prev is None or n == prev + 1:
            seq += 1
            prev = n
            ans = max(ans, seq)
        elif n != prev:
            seq = 1
            prev = n

    ans = max(ans, seq)
    print(f'ans = {ans}')

    res = sol.longest_consecutive2(inp)
    print(f'{res} == {ans}')


# test()
random_test()
