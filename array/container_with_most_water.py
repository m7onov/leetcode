"""
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/830/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:

.. image:: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of
water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""
import sys
import cProfile
from typing import List
from random import randint


def log(msg):
    # print(msg)
    pass


class Solution:
    def max_area_brute_force(self, height: List[int]) -> int:
        max_area = 0
        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height[i + 1:], i + 1):
                area = (j - i) * min(h1, h2)
                log(f'({j} - {i}) * min({h1}, {h2}) = {area}')
                if area > max_area:
                    max_area = area
        return max_area

    def max_area_1(self, height: List[int]) -> int:
        hln = len(height)
        height_with_idx = [t for t in enumerate(height)]
        height_with_idx.sort(key=lambda x: x[1])
        height_sorted = [i[1] for i in height_with_idx]
        height_idx = [i[0] for i in height_with_idx]
        log(f'{height_sorted} - height_sorted')
        log(f'{height_idx} - height_idx')
        left = hln
        right = 0
        left_arr = [-1] * hln
        right_arr = [-1] * hln
        for i in range(hln - 1, -1, -1):
            if height_idx[i] < left:
                left = height_idx[i]
            if height_idx[i] > right:
                right = height_idx[i]
            left_arr[i] = left
            right_arr[i] = right

        max_area = 0
        for i in range(hln):
            left_len = abs(height_idx[i] - left_arr[i])
            right_len = abs(height_idx[i] - right_arr[i])
            area = height_sorted[i] * max(left_len, right_len)
            max_area = max(area, max_area)

        log(f'{left_arr} - left_arr')
        log(f'{right_arr} - right_arr')
        return max_area

    def max_area_2(self, height: List[int]) -> int:
        left_idx = 0
        right_idx = len(height) - 1
        max_area = float('-inf')
        while left_idx < right_idx:
            area = (right_idx - left_idx) * min(height[left_idx], height[right_idx])
            max_area = max(max_area, area)
            if height[left_idx] < height[right_idx]:
                left_idx += 1
            else:
                right_idx -= 1
        return max_area


def test():
    sol = Solution()
    res = sol.max_area_2([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(res)


def random_tests(num=1000):
    sol = Solution()
    for _ in range(num):
        height = [randint(0, 10**4) for _ in range(10**3)]
        res_bf = sol.max_area_brute_force(height)
        res = sol.max_area_2(height)
        if res_bf != res:
            print(height, file=sys.stderr)
            raise Exception('error')


def perf_test():
    sol = Solution()
    height = [randint(0, 10**4) for _ in range(10**5)]
    stats = cProfile.runctx('sol.max_area(height)', globals=globals(), locals=locals(), sort=2)


test()
# random_tests()
# perf_test()
