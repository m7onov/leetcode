"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3570/

Given an integer array nums, return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""
from typing import List


class Solution:

    @staticmethod
    def increasing_triplet_dumb(nums: List[int]) -> bool:

        def scan_next(prev_idx: int, depth: int) -> bool:
            for i in range(prev_idx + 1, len(nums)):
                if prev_idx == -1 or nums[i] > nums[prev_idx]:
                    if depth == 3:
                        return True
                    else:
                        if scan_next(i, depth + 1):
                            return True

            return False

        return scan_next(-1, 1)

    @staticmethod
    def increasing_triplet_smart(nums: List[int]) -> bool:
        first_num = None
        second_num = None
        for n in nums:
            # Note: на каждой итерации у нас будет минимальное и предминимальное число из тех,
            # что мы уже видели; ветка else сработает только если очередное число больше минимального и
            # предминимального
            if first_num is None or n <= first_num:
                # Note: будем попадать сюда каждый раз когда очередное число меньше или равно предыдущему
                #       наименьшему; то есть эта ветка для поиска минимального значения
                first_num = n
            elif second_num is None or n <= second_num:
                # Note: сюда попадём только если очередное число больше, чем first_num
                second_num = n
            else:
                # Note: сюда попадём только если очередное число больше, чем first_num и second_num
                return True

        return False


# print(Solution().increasing_triplet_dumb([1, 2, 3, 4, 5]))
# print(Solution().increasing_triplet_dumb([5, 4, 3, 2, 1]))
# print(Solution().increasing_triplet_dumb([2, 1, 5, 0, 4, 6]))
# print(Solution().increasing_triplet_dumb([2, 4, -2, -3]))
# print(Solution().increasing_triplet_dumb([2, 5, 3, 4, 5]))
