"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/

Given an integer array nums, design an algorithm to randomly shuffle the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.

Example 1:
Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must be equally
                       // likely to be returned. Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

Constraints:
1 <= nums.length <= 200
-10^6 <= nums[i] <= 10^6
All the elements of nums are unique.
At most 5 * 10^4 calls will be made to reset and shuffle.
"""
from typing import List
from random import randint
from collections import defaultdict


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle_brute_force(self) -> List[int]:
        n = len(self.nums)
        ret_list = []
        aux_list = self.nums.copy()
        for i in range(n):
            j = randint(0, n - 1 - i)
            ret_list.append(aux_list.pop(j))

        return ret_list

    def shuffle_fisher_yates(self) -> List[int]:
        n = len(self.nums)
        ret_list = self.nums.copy()
        for i in range(n - 1):
            j = randint(i, n - 1)
            ret_list[i], ret_list[j] = ret_list[j], ret_list[i]

        return ret_list


obj = Solution([1, 2, 3])

m = defaultdict(int)
for _i in range(10000):
    v = "".join([str(i) for i in obj.shuffle_fisher_yates()])
    m[v] += 1

print('\n'.join([str(i) for i in m.values()]))
