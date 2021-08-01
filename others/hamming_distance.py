"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/

The Hamming distance (https://en.wikipedia.org/wiki/Hamming_distance) between two integers is the number of positions
at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.

Example 1:
Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example 2:
Input: x = 3, y = 1
Output: 1

Constraints:
0 <= x, y <= 2^31 - 1
"""


class Solution:
    def hamming_distance(self, x: int, y: int) -> int:
        s = 0
        i, j, d = x, y, 0
        while i > 0 and j > 0:
            if (i % 2) != (j % 2):
                s += 1
            i = i // 2
            j = j // 2

        if i > 0:
            d = i
        else:
            d = j

        while d > 0:
            if d % 2 == 1:
                s += 1
            d = d // 2

        return s

    def hamming_distance2(self, x: int, y: int) -> int:
        z = x ^ y
        s = 0
        while z > 0:
            if z % 2 == 1:
                s += 1
            z = z // 2
        return s

    def hamming_distance3(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

    def hamming_distance4(self, x: int, y: int) -> int:
        # !smart approach
        # http://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan
        s = 0
        z = x ^ y
        while z > 0:
            s += 1
            z = z & (z - 1)
        return s


sol = Solution()
print(sol.hamming_distance4(1, 4))  # 2
print(sol.hamming_distance4(3, 1))  # 1
print(sol.hamming_distance4(983745684376, 92837564100))  # 19


