"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3567/

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""
from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    abs_min_n = (0, abs(nums[0]))
    for i, n in enumerate(nums):
        if abs(n) < abs_min_n[1]:
            abs_min_n = (i, abs(n))

    ret_list = [abs_min_n[1] ** 2]

    ln = len(nums)
    i = abs_min_n[0] - 1
    j = abs_min_n[0] + 1
    while i >= 0 or j < ln:
        left = None
        right = None
        if i >= 0:
            left = nums[i]

        if j < ln:
            right = nums[j]

        if left is None:
            ret_list.append(right ** 2)
            j += 1

        elif right is None:
            ret_list.append(left ** 2)
            i -= 1

        elif abs(left) <= abs(right):
            ret_list.append(left ** 2)
            i -= 1

        else:
            ret_list.append(right ** 2)
            j += 1

    return ret_list


# вот это - читерство и вообще не спортивно
def sorted_squares2(nums: List[int]) -> List[int]:
    nums = [n**2 for n in nums]
    nums.sort()
    return nums


print(sorted_squares([-7, -3, 2, 3, 11]))
