"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/743/

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.

Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:
1 <= n <= 10^4
"""
from typing import List


class Solution:

    def fizz_buzz(self, n: int) -> List[str]:
        ret_arr = []
        for i in range(1, n+1):
            element = ""
            if i % 3 == 0:
                element = "Fizz"
            if i % 5 == 0:
                element += "Buzz"
            if element == "":
                element = str(i)

            ret_arr.append(element)

        return ret_arr


sol = Solution()
print(sol.fizz_buzz(3))
print(sol.fizz_buzz(5))
print(sol.fizz_buzz(15))
