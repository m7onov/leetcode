"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def three_sum_with_2pointers(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        np = None
        for i, n in enumerate(nums):
            if n == np:
                continue
            if n > 0:
                break

            np = n
            l = i + 1
            h = len(nums) - 1
            while l < h:
                sm = n + nums[l] + nums[h]
                if sm < 0:
                    l = l + 1
                elif sm > 0:
                    h = h - 1
                else:
                    result.append([n, nums[l], nums[h]])
                    lp = l
                    while l < h and nums[l] == nums[lp]:
                        l = l + 1
                    hp = h
                    while h > l and nums[h] == nums[hp]:
                        h = h - 1

        return result

    def three_sum_with_hashes(selfs, nums: List[int]) -> List[List[int]]:
        def log(msg):
            pass

        result = []
        nums = sorted(nums)
        nums_len = len(nums)
        n_previous = None
        for i, n in enumerate(nums):
            if n > 0:
                break
            if n == n_previous:
                continue
            log(f'n = {n}')
            seen = set()
            nli = i+1
            while nli < nums_len:
                nl = nums[nli]
                nli += 1
                log(f'searching: {-n-nl}')
                if -n-nl in seen:
                    log(f'append to result: {n, nl, -n-nl}')
                    result.append([n, nl, -n-nl])
                    while nli < nums_len and nums[nli] == nl:
                        nli += 1
                log('add to seen: ' + str(nl))
                seen.add(nl)
            n_previous = n
        return result


sol = Solution()
print(sol.three_sum_with_2pointers([-1, 0, 1, 2, -1, -4]))
print(sol.three_sum_with_2pointers([]))
print(sol.three_sum_with_2pointers([0]))
print(sol.three_sum_with_2pointers([0, 0, 0]))

print(sol.three_sum_with_hashes([-1, 0, 1, 2, -1, -4]))
print(sol.three_sum_with_hashes([]))
print(sol.three_sum_with_hashes([0]))
print(sol.three_sum_with_hashes([0, 0, 0]))
