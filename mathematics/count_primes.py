"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/

Count the number of prime numbers less than a non-negative number, n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:
0 <= n <= 5 * 10^6
"""
import time

from math import sqrt


class Solution:
    def count_primes2(self, n: int) -> int:
        primes = []
        is_odd = False
        for i in range(2, n):
            if is_odd:
                is_prime = True
                for j in primes:
                    if i % j == 0:
                        is_prime = False
                        break
                    elif j > i / 2:
                        break
                if is_prime:
                    primes.append(i)
            elif i == 2:
                primes.append(i)
            is_odd = not is_odd
        return len(primes)

    def count_primes3(self, n: int) -> int:
        primes = []
        is_odd = False
        for i in range(2, n):
            if is_odd:
                is_prime = True
                for j in primes:
                    if i % j == 0:
                        is_prime = False
                        break
                    elif j > sqrt(i):
                        break
                if is_prime:
                    primes.append(i)
            elif i == 2:
                primes.append(i)
            is_odd = not is_odd
        return len(primes)

    def count_primes4(self, n: int) -> int:
        if n == 0:
            return 0
        sieve = [True for _ in range(n + 1)]
        sieve[0] = False
        sieve[1] = False
        for prime in range(2, int(sqrt(n)) + 1):
            if sieve[prime]:
                j = 2 * prime
                while j < n + 1:
                    sieve[j] = False
                    j += prime
        counter = 0
        for prime in sieve[1:-1]:
            if prime:
                counter += 1
        return counter

    def count_primes5(self, n: int) -> int:
        if n == 0:
            return 0
        sieve = [True for _ in range(n + 1)]
        sieve[0] = False
        sieve[1] = False
        for prime in range(2, int(sqrt(n)) + 1):
            if sieve[prime]:
                j = prime * prime
                while j < n + 1:
                    sieve[j] = False
                    j += prime
        counter = 0
        for prime in sieve[1:-1]:
            if prime:
                counter += 1
        return counter

    def count_primes6(self, n: int) -> int:
        if n <= 2:
            return 0
        numbers = {}
        for p in range(2, int(sqrt(n)) + 1):
            if p not in numbers:
                for multiple in range(p * p, n, p):
                    numbers[multiple] = 1
        # Exclude "1" and the number "n" itself.
        return n - len(numbers) - 2


times = []
for i in range(10):
    start_time = time.monotonic()
    Solution().count_primes6(100000)
    times.append(time.monotonic() - start_time)

print('avg = ', round(sum(times) / len(times), 3))

# print(Solution().count_primes5(100000))
# print(Solution().count_primes5_1(100000))
