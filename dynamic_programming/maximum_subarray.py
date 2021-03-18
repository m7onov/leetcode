"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and
return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [0]
Output: 0

Example 4:
Input: nums = [-1]
Output: -1

Example 5:
Input: nums = [-100000]
Output: -100000

Constraints:
1 <= nums.length <= 3 * 10^4
-10^5 <= nums[i] <= 10^5

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.

NOTE: связанные задачи
https://leetcode.com/problems/gas-station/
https://leetcode.com/problems/super-washing-machines/
https://leetcode.com/problems/sliding-window-maximum/
"""
from typing import List


def max_sub_array(nums: List[int]) -> int:
    start_idx = None
    rolling_sum = None
    max_rolling_sum = None
    max_rolling_sum_start_idx = None
    max_rolling_sum_end_idx = None
    max_element = None
    max_element_idx = None
    for i, n in enumerate(nums):
        if max_element is None or n > max_element:
            max_element = n
            max_element_idx = i

        if rolling_sum == None:
            if n <= 0:
                continue
            else:
                start_idx = i
                rolling_sum = n
        else:
            if rolling_sum + n < 0:
                start_idx = None
                rolling_sum = None
                continue
            else:
                rolling_sum += n

        if max_rolling_sum is None or rolling_sum > max_rolling_sum:
            max_rolling_sum = rolling_sum
            max_rolling_sum_start_idx = start_idx
            max_rolling_sum_end_idx = i

    if max_rolling_sum is None:
        return max_element, max_element_idx, max_element_idx
    else:
        return max_rolling_sum, max_rolling_sum_start_idx, max_rolling_sum_end_idx


def max_sub_array_divide_and_conquer(nums: List[int]) -> int:
    def cross_sum(rnums, left, right, p):
        if left == right:
            return nums[left]

        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(p, left - 1, -1):
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)

        right_subsum = float('-inf')
        curr_sum = 0
        for i in range(p + 1, right + 1):
            curr_sum += nums[i]
            right_subsum = max(right_subsum, curr_sum)

        return left_subsum + right_subsum

    def helper(nums, left, right):
        if left == right:
            return nums[left]

        p = (left + right) // 2

        left_sum = helper(nums, left, p)
        right_sum = helper(nums, p + 1, right)
        cross_sum_val = cross_sum(nums, left, right, p)

        return max(left_sum, right_sum, cross_sum_val)

    return helper(nums, 0, len(nums) - 1)


print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
print(max_sub_array([1]))
print(max_sub_array([0]))
print(max_sub_array([-1]))
print(max_sub_array([-100000]))

print(max_sub_array_divide_and_conquer([-2,1,-3,4,-1,2,1,-5,4]))
print(max_sub_array_divide_and_conquer([1]))
print(max_sub_array_divide_and_conquer([0]))
print(max_sub_array_divide_and_conquer([-1]))
print(max_sub_array_divide_and_conquer([-100000]))
