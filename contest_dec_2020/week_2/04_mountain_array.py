"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3561/

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
    - arr.length >= 3
    - There exists some i with 0 < i < arr.length - 1 such that:
      arr[0] < arr[1] < ... < arr[i - 1] < A[i]
      arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true

Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 104
"""
from typing import List


def valid_mountain_array(arr: List[int]) -> bool:
    ln = len(arr)
    if 0 < ln < 3:
        return False

    top_idx = 0
    while top_idx < ln - 1 and arr[top_idx + 1] > arr[top_idx]:
        top_idx += 1

    if top_idx == 0 or top_idx == ln - 1:
        return False

    while top_idx < ln - 1:
        if arr[top_idx + 1] >= arr[top_idx]:
            return False
        else:
            top_idx += 1

    return True


print(valid_mountain_array([2, 1]))
print(valid_mountain_array([3, 5, 5]))
print(valid_mountain_array([0, 3, 2, 1]))
