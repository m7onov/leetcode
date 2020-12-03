"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/96/sorting-and-searching/587/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]

Constraints:
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
"""
from typing import List


def merge2(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = m - 1
    j = n - 1
    k = m + n - 1

    while k >= 0:
        if i < 0:
            v = nums2[j]
            j -= 1
        elif j < 0:
            v = nums1[i]
            i -= 1
        elif nums1[i] < nums2[j]:
            v = nums2[j]
            j -= 1
        else:
            v = nums1[i]
            i -= 1

        nums1[k] = v
        k -= 1


# b = [4, 5, 6, 7, 13, 14]
# a = [1, 2, 3, 10, 11, 12] + ([None] * len(b))
# al = 6
# bl = 6

# b = [3]
# a = [1, 2, 4, 5, 6, 0]
# al = 5
# bl = 1

a = [0]
b = [1]
al = 0
bl = 1

merge2(a, al, b, bl)
print(a)
