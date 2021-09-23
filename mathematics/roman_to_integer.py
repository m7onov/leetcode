"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply
X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
    - I can be placed before V (5) and X (10) to make 4 and 9.
    - X can be placed before L (50) and C (100) to make 40 and 90.
    - C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3

Example 2:
Input: s = "IV"
Output: 4

Example 3:
Input: s = "IX"
Output: 9

Example 4:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
It is guaranteed that s is a valid roman numeral in the range [1, 3999]
"""


class Solution:
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    def roman_to_int(self, s: str) -> int:
        sm = self.romans[s[0]]
        for i in range(1, len(s)):
            dc = self.romans[s[i]]
            sm += dc
            for j in range(i - 1, -1, -1):
                dp = self.romans[s[j]]
                if dp < dc:
                    sm -= (2*dp)
                else:
                    break

        return sm

    def roman_to_int2(self, s: str) -> int:
        sm = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in self.romans:
                sm += self.romans[s[i:i+2]]
                i += 2
            else:
                sm += self.romans[s[i]]
                i += 1

        return sm

    def roman_to_int3(self, s: str) -> int:
        sm = 0
        prev = None
        for i in range(len(s)-1, -1, -1):
            cur = self.romans[s[i]]
            if prev is not None and cur < prev:
                sm -= cur
            else:
                sm += cur
            prev = cur
        return sm


print(Solution().roman_to_int("III"))
print(Solution().roman_to_int("IV"))
print(Solution().roman_to_int("IX"))
print(Solution().roman_to_int("XXVII"))
print(Solution().roman_to_int("LVIII"))
print(Solution().roman_to_int("MCMXCIV"))

print("---------------------------------------")

print(Solution().roman_to_int2("III"))
print(Solution().roman_to_int2("IV"))
print(Solution().roman_to_int2("IX"))
print(Solution().roman_to_int2("XXVII"))
print(Solution().roman_to_int2("LVIII"))
print(Solution().roman_to_int2("MCMXCIV"))

print("---------------------------------------")

print(Solution().roman_to_int3("III"))
print(Solution().roman_to_int3("IV"))
print(Solution().roman_to_int3("IX"))
print(Solution().roman_to_int3("XXVII"))
print(Solution().roman_to_int3("LVIII"))
print(Solution().roman_to_int3("MCMXCIV"))
