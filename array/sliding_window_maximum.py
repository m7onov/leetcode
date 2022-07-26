"""
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/837/

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the
array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one
position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""
from typing import List
from collections import deque
import heapq


class Solution:
    # O(N * K) overall
    def max_sliding_window_dumb(self, nums: List[int], k: int) -> List[int]:
        w_max_array = []
        window = [0] * k
        window_index = 0
        w_cur_max = float('-inf')
        for i, n in enumerate(nums):
            replaced_n = window[window_index]
            window[window_index] = n
            window_index = (window_index + 1) % k
            if i + 1 >= k:
                if n >= w_cur_max:
                    w_cur_max = n
                elif replaced_n == w_cur_max:
                    # O(k)
                    w_cur_max = max(window)
                w_max_array.append(w_cur_max)
            else:
                w_cur_max = max(w_cur_max, n)
        return w_max_array

    def max_sliding_window_dumb_improved1(self, nums: List[int], k: int) -> List[int]:
        """
        Случай 1 - при каждом шаге из окна выпадает максимальный элемент, каждый раз приходится искать максимальный
        элемент в окне за O(k) время
        9 8 7 6 5 4 3 2 1
        - - -

        Случай 2 - при каждом шаге из окна выпадают все элементы, кроме максимального; каждый раз приходится искать
        максимальный элемент среди двух за O(1) время
        1 2 3 4 5 6 7 8 9
        - - -
        """
        w_max_array = []
        window = deque()

        for i, n in enumerate(nums):
            window.append(n)

            if len(window) > k:
                window.popleft()

            if i + 1 >= k:
                w_cur_max = max(window)
                while window[0] < w_cur_max:
                    window.popleft()

                w_max_array.append(w_cur_max)

        return w_max_array

    def max_sliding_window_dumb2(self, nums: List[int], k: int) -> List[int]:
        w_max_array = []
        window = [0] * k
        window_index = 0
        w_cur_max = float('-inf')
        window_heap = []
        for i, n in enumerate(nums):
            replaced_n = window[window_index]
            window[window_index] = n
            window_index = (window_index + 1) % k
            if (i + 1) >= k:
                if n >= w_cur_max:
                    if len(window_heap) == 0:
                        heapq.heappush(window_heap, -n)
                    else:
                        heapq.heapreplace(window_heap, -n)
                    w_cur_max = n
                elif replaced_n == w_cur_max:
                    heapq.heapreplace(window_heap, -n)
                    w_cur_max = -1 * window_heap[0]
                else:
                    heapq.heappush(window_heap, -n)

                w_max_array.append(w_cur_max)
            else:
                w_cur_max = max(w_cur_max, n)
                heapq.heappush(window_heap, -n)
        return w_max_array

    # O(N * log(K)) overall
    def max_sliding_window_binsearch(self, nums: List[int], k: int) -> List[int]:
        def bin_search_index(arr, start_idx, end_idx, val):
            if start_idx == end_idx:
                return start_idx
            mid_idx = (start_idx + end_idx) // 2
            if arr[mid_idx] >= val:
                return bin_search_index(arr, start_idx, mid_idx, val)
            else:
                return bin_search_index(arr, mid_idx + 1, end_idx, val)

        w_max_array = []
        window = [float('-inf')] * k
        window_sorted = None
        window_index = 0
        w_cur_max = float('-inf')
        for i, n in enumerate(nums):
            replaced_n = window[window_index]
            window[window_index] = n
            window_index = (window_index + 1) % k

            if i + 1 < k:
                w_cur_max = max(w_cur_max, n)
            else:
                if i + 1 == k:
                    window_sorted = list(sorted(window))

                print(window_sorted, n, w_cur_max, replaced_n)

                if n >= w_cur_max:
                    w_cur_max = n
                elif replaced_n == w_cur_max:
                    if k > 2:
                        idx = bin_search_index(window_sorted, 0, k - 2, n)
                    else:
                        idx = 0

                    print(f'window_sorted = {window_sorted}')
                    print(f'{n} index = {idx}')

                    if idx + 1 == k - 1:
                        window_sorted[k - 1] = n
                    else:
                        window_sorted.insert(idx + 1, n)
                    w_cur_max = window_sorted[-1]

                w_max_array.append(w_cur_max)

        return w_max_array

    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        return self.max_sliding_window_dumb_improved1(nums, k)


def tests():
    sol = Solution()
    for nums, k, ans in [
                         ([1, 3, 1, 2, 0, 5], 3, [3, 3, 2, 5]),
                         ([7, 2, 4], 2, [7, 4]),
                         ([1, -1], 1, [1, -1]),
                         ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
                         ([1], 1, [1]),
                         ([-7, -8, 7, 5, 7, 1, 6, 0], 4, [7, 7, 7, 7, 7])
                        ]:
        res = sol.max_sliding_window(nums, k)
        print(f'{nums} -> {res} == {ans} ({res == ans})')


tests()

# def bin_search_index(arr, start_idx, end_idx, n):
#     if start_idx == end_idx:
#         return start_idx
#     mid_idx = (start_idx + end_idx) // 2
#     if arr[mid_idx] >= n:
#         return bin_search_index(arr, start_idx, mid_idx, n)
#     else:
#         return bin_search_index(arr, mid_idx + 1, end_idx, n)
#
#
# ans = bin_search_index([2, 6], 0, 1, 2)
# print(ans)
