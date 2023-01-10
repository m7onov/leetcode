"""
https://leetcode.com/explore/interview/card/top-interview-questions-hard/116/array-and-strings/834/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Constraints:
    1 <= n <= 10^5
    nums.length == n + 1
    1 <= nums[i] <= n
    All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:
    How can we prove that at least one duplicate number must exist in nums?
    Can you solve the problem in linear runtime complexity?
"""
from typing import List
from math import ceil, floor, log2
from random import randint, shuffle
from collections import defaultdict


class Solution:
    def find_duplicate_dumb(self, nums: List[int]):
        # O(n), O(n)
        a = defaultdict(int)
        for n in nums:
            a[n] += 1
        return max(a.items(), key=lambda x: x[1])[0]

    def find_duplicate_nonlinear1(self, nums: List[int]) -> int:
        # O(n^2), O(1)
        batch_size = 1000
        s = set()
        for i in range(ceil(len(nums) / batch_size)):
            s.clear()
            for j in range(batch_size*i, len(nums)):
                if nums[j] in s:
                    return nums[j]
                s.add(nums[j])

    def find_duplicate_nonlinear2(self, nums: List[int]) -> int:
        # O(n^2), O(1)
        start_num = 1
        stop_num = len(nums) - 1

        while start_num != stop_num:
            avg = (start_num + stop_num) / 2
            left_count = sum([1 for x in nums if start_num <= x <= avg])
            right_count = sum([1 for x in nums if avg <= x <= stop_num])

            print(f'start_num = {start_num}, stop_num = {stop_num}, avg = {avg}, '
                  f'left_count = {left_count}, right_count = {right_count}')

            if left_count > right_count:
                stop_num = floor(avg)
            else:
                start_num = ceil(avg)

        return start_num

    def find_duplicate_linear1(self, nums: List[int]) -> int:
        # O(n), O(1)
        # NOTE: not a solution since input list is modified
        for n in nums:
            n_abs = abs(n)
            if nums[n_abs] < 0:
                return n_abs
            else:
                nums[n_abs] *= -1
        raise Exception('unexpected')

    def find_duplicate_linear2(self, nums: List[int]) -> int:
        # O(n), O(1)
        # NOTE: not a solution since input list is modified
        for _ in range(len(nums)):
            nums0 = nums[0]
            if nums[nums0] == nums0:
                return nums0
            else:
                nums[0], nums[nums0] = nums[nums0], nums0
        raise Exception('unexpected')

    def find_duplicate_bs(self, nums: List[int]) -> int:
        # O(n*log(n)), O(1)
        from_num = 1
        to_num = len(nums) - 1
        while from_num < to_num:
            mid_num = (from_num + to_num) // 2
            cur_cnt = sum(1 for x in nums if x <= mid_num)
            if cur_cnt <= mid_num:
                from_num = mid_num + 1
            else:
                to_num = mid_num

        if from_num < to_num:
            raise Exception('unexpected')

        return from_num

    """
    x x x x x x x x x x x x
    # Исходная последовательность
    0 0 0 0 0 0 0 0 0 0 0 1 - 1
    0 0 0 0 0 0 0 0 0 0 1 0 - 2
    0 0 0 0 0 0 0 0 0 0 1 1 - 3
    0 0 0 0 0 0 0 0 0 1 0 0 - 4
    0 0 0 0 0 0 0 0 0 1 0 1 - 5
    ----
    0 0 0 0 0 0 0 0 0 2 2 3 - счётчики
    
    # (А) Добавляем один лишний элемент (всегда по условию)
    0 0 0 0 0 0 0 0 0 0 0 1 - 1
    0 0 0 0 0 0 0 0 0 0 1 0 - 2
    0 0 0 0 0 0 0 0 0 0 1 1 - 3
    0 0 0 0 0 0 0 0 0 1 0 0 - 4
    0 0 0 0 0 0 0 0 0 1 0 1 - 5
    0 0 0 0 0 0 0 0 0 0 0 1 - 1 *
    ----
    0 0 0 0 0 0 0 0 0 2 2 4 - счётчики
    # Счётчики увеличиваются в тех разрядах, в которых искомое число имеет значение 1
    # при этом разница в каждом из счётчиков не больше 1 и не меньше 0
    
    # (Б) Добавляем ещё один лишний элемент __взамен__ другого (не всегда; можно заменить не один)
    0 0 0 0 0 0 0 0 0 0 0 1 - 1
    0 0 0 0 0 0 0 0 0 0 1 0 - 2
    0 0 0 0 0 0 0 0 0 0 0 1 - 1 *
    0 0 0 0 0 0 0 0 0 1 0 0 - 4
    0 0 0 0 0 0 0 0 0 1 0 1 - 5
    0 0 0 0 0 0 0 0 0 0 0 1 - 1
    ----
    0 0 0 0 0 0 0 0 0 2 1 4 - счётчики
    # Смотрим каждый разряд искомого и заменённого числа по отдельности (искомое --> заменённое)
    1 --> 1 сумма счётчика не меняется
    0 --> 0 сумма счётчика не меняется
    1 --> 0 сумма счётчика увеличивается
    0 --> 1 сумма счётчика уменьшается
    - Если разряд искомого числа 1, а заменённого 0, то счётчик увеличивается. В этом случае с учётом (А) (разница 
      счётчиков не меньше 0) счётчик переходит в 1 или большее число.
    - Если разряд искомого числа 0, а заменённого 1, то счётчик уменьшается. В этом случае с учётом (А) (разница 
      счётчиков не больше 1) счётчик переходит в 0 или становится отрицательным.
    - В других комбинациях разрядов искомого и заменённого чисел счётчики не меняются.
    - Таким образом, в результате (Б), счётчики в 0-вых разрядах искомого числа будут стремиться к уменьшению и будут 
      меньше или равны 0, а счётчики в 1-ых разрядах искомого числа будут стремиться к увеличению и будут больше или
      равны 1.
    """
    def find_duplicate_bits1(self, nums: List[int]) -> int:
        # num_bits ~ O(log2(N)) => по времени O(N*log(N))
        # по памяти - O(log(N))
        num_bits = ceil(log2(len(nums)))
        exp_counters = [0] * num_bits
        counters = [0] * num_bits
        for i, n in enumerate(nums):
            for j in range(num_bits):
                if (i >> j) & 1 == 1:
                    exp_counters[j] += 1
                if (n >> j) & 1 == 1:
                    counters[j] += 1

        ret_val = 0
        for j in range(num_bits):
            if counters[j] > exp_counters[j]:
                ret_val += (2 ** j)

        return ret_val

    def find_duplicate_bits2(self, nums: List[int]) -> int:
        # num_bits ~ O(log2(N)) => по времени O(N*log(N))
        # по памяти - O(log(N))
        # NOTE: хотя вроде нет особой разницы в сравнении с find_duplicate_bits1
        nums_len = len(nums)
        num_bits = ceil(log2(nums_len))
        ret_val = 0
        for bit_idx in range(num_bits):
            exp_counter = 0
            counter = 0
            for j, n in enumerate(nums, start=1):
                if j < nums_len:
                    exp_counter += ((j >> bit_idx) & 1)
                counter += ((n >> bit_idx) & 1)
            if counter > exp_counter:
                ret_val += (2 ** bit_idx)

        return ret_val

    def find_duplicate_tortoise_and_hare(self, nums: List[int]) -> int:
        nums_len = len(nums)
        tortoise_val = nums[0]
        hare_val = nums[0]
        phase = 1

        def next_val(cur_idx: int, incr: int) -> int:
            new_idx = cur_idx
            for _ in range(incr):
                new_idx = nums[new_idx]
            return new_idx

        for i in range(2 * nums_len):
            # print(f'{i}: tortoise_val = {tortoise_val}, hare_val = {hare_val}')
            tortoise_val = next_val(tortoise_val, 1)
            hare_val = next_val(hare_val, 2 if phase == 1 else 1)
            if tortoise_val == hare_val:
                # print(f'i = {i}, phase = {phase}, tortoise_val = {tortoise_val}, hare_val = {hare_val}')
                if phase == 1:
                    tortoise_val = nums[0]
                    phase = 2
                if phase == 2 and tortoise_val == hare_val:
                    return tortoise_val

        raise Exception('unexpected')

    def find_duplicate(self, nums: List[int]) -> int:
        return self.find_duplicate_tortoise_and_hare(nums)


def specific_tests():
    sol = Solution()
    res = sol.find_duplicate([1, 3, 4, 2, 2])
    print(res)
    res = sol.find_duplicate([3, 1, 3, 4, 2])
    print(res)
    res = sol.find_duplicate([1, 2, 2, 2, 4])
    print(res)
    res = sol.find_duplicate([1, 1])
    print(res)
    res = sol.find_duplicate([1, 2, 3, 4, 5, 4, 4, 4, 4, 4])
    print(res)
    res = sol.find_duplicate([76, 2, 92, 79, 89, 48, 70, 11, 73, 86, 19, 60, 39, 30, 56, 55, 13, 17, 46, 29, 52, 90, 88,
                              40, 18, 64, 41, 44, 59, 65, 20, 49, 59, 4, 47, 93, 5, 24, 38, 75, 84, 99, 59, 82, 54, 94,
                              28, 14, 83, 27, 85, 53, 37, 35, 25, 67, 68, 42, 23, 63, 51, 71, 31, 74, 34, 80, 59, 22,
                              50, 8, 3, 58, 32, 77, 91, 96, 59, 9, 61, 98, 59, 95, 12, 21, 72, 7, 62, 59, 66, 10, 69,
                              81, 6, 33, 45, 100, 15, 36, 16, 57, 43])
    print(res)  # 59
    res = sol.find_duplicate([3, 2, 2, 2, 4])
    print(res)


def generate_random_test(nums_len=100):
    nums = [i for i in range(1, nums_len+1)]
    dup = randint(1, nums_len)
    for i in range(randint(1, min(10, nums_len))):
        nums[randint(0, nums_len-1)] = dup
    nums.append(dup)
    shuffle(nums)
    return nums, dup


def do_random_test():
    nums, dup = generate_random_test(15)
    sol = Solution()
    ans = sol.find_duplicate(nums)
    print(f'{ans} = {dup}')
    if ans != dup:
        print('nums is ', nums)
        print('dup is ', dup)
        raise Exception('wrong answer')


for _ in range(100):
    do_random_test()

# specific_tests()
