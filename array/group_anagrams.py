"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""
from typing import List
from collections import defaultdict
from random import choice, randint
import timeit


class Solution:
    # O(L*W*log(W)) - speed
    # O(L*W) - memory
    def groupAnagramsWithSorting(self, strs: List[str]) -> List[List[str]]:
        strs1 = sorted(strs, key=len)
        strs2 = [''.join(sorted(s)) for s in strs1]
        anagrams = defaultdict(list)
        for i, s in enumerate(strs2):
            anagrams[s].append(strs1[i])

        return [v for v in anagrams.values()]

    # O(L*W) - speed
    # O(L*W) - memory
    def groupAnagramsWithCounters(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            s_key = [0] * (ord('z') - ord('a') + 1)
            for c in s:
                s_key[ord(c) - ord('a')] += 1
            anagrams[tuple(s_key)].append(s)

        return [v for v in anagrams.values()]


sol = Solution()
res = sol.groupAnagramsWithSorting(["eat", "tea", "tan", "ate", "nat", "bat"])
print(res)
res = sol.groupAnagramsWithSorting(["", "b", ""])
print(res)
res = sol.groupAnagramsWithCounters(["eat", "tea", "tan", "ate", "nat", "bat"])
print(res)
res = sol.groupAnagramsWithCounters(["", "b", ""])
print(res)


def perfomance_test():
    def generate_random_input():
        result = []
        d = [chr(o) for o in range(ord('a'), ord('z') + 1)]
        for _ in range(randint(0, 10000)):
            l = randint(0, 101)
            random_string = ''.join(choice(d) for _ in range(l))
            result.append(random_string)
        return result

    def perform_batch_test_with_sorting():
        for indata in indatas:
            Solution().groupAnagramsWithSorting(indata)

    def perform_batch_test_with_counters():
        for indata in indatas:
            Solution().groupAnagramsWithCounters(indata)

    indatas = [generate_random_input() for _ in range(100)]
    measured_time = timeit.timeit(lambda: perform_batch_test_with_sorting(), number=10)
    print(f'with sorting: {measured_time}')
    measured_time = timeit.timeit(lambda: perform_batch_test_with_counters(), number=10)
    print(f'with counters: {measured_time}')
