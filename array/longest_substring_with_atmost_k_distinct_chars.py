"""
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/835/

Given a string s and an integer k, return the length of the longest substring of s that contains at most k
distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

Constraints:
1 <= s.length <= 5 * 10^4
0 <= k <= 50
"""
from collections import defaultdict


class Solution:
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # O(N) time complexity
        # O(k) memory complexity
        max_len = 0
        char_map = defaultdict(int)
        total_len = 0
        from_idx = 0
        for i, ci in enumerate(s):
            char_map[ci] += 1
            while len(char_map) > k:
                cj = s[from_idx]
                char_map[cj] -= 1
                total_len -= 1
                from_idx += 1
                if char_map[cj] == 0:
                    del char_map[cj]

            total_len += 1
            max_len = max(total_len, max_len)
            print(f'{char_map}, {total_len}, {max_len}')

        return max_len


def test():
    sol = Solution()
    for s, k in [('eceba', 2), ('aa', 1)]:
        res = sol.length_of_longest_substring_k_distinct(s, k)
        print(f'{s} -> {res}')


test()
