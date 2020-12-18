"""
https://leetcode.com/problems/4sum-ii/solution/

this is a generalized idea
"""
from collections import defaultdict
from typing import List


def ksum(arrs: List[List[int]]) -> int:
    num_combinations = 0
    counters = defaultdict(int)

    def for_each_combination_sum(prefix_sum: int, arr_idx_from: int, arr_idx_to: int, action):
        if arr_idx_from < arr_idx_to - 1:
            for n in arrs[arr_idx_from]:
                for_each_combination_sum(prefix_sum + n, arr_idx_from + 1, arr_idx_to, action)

        else:
            for n in arrs[arr_idx_from]:
                action(prefix_sum, n)

    def incr_counter(prefix_sum, n):
        counters[-prefix_sum - n] += 1

    def check_counter(prefix_sum, n):
        nonlocal num_combinations
        num_combinations += counters[prefix_sum + n]

    for_each_combination_sum(0, 0, len(arrs) // 2, incr_counter)
    for_each_combination_sum(0, len(arrs) // 2, len(arrs), check_counter)

    return num_combinations


print(ksum([[1, 2],
            [-2, -1],
            [-1, 2],
            [0, 2]]))