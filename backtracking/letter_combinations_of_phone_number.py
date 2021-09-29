"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/793/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map
to any letters.

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
    | 0 <= digits.length <= 4
    | digits[i] is a digit in the range ['2', '9'].
"""
from typing import List


def letter_combinations(digits: str) -> List[str]:
    digit2letters = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    result = []
    counters = [0] * len(digits)
    the_end = not len(counters) > 0
    while not the_end:
        res = []
        for i, d in enumerate(digits):
            res.append(digit2letters[d][counters[i]])

        result.append(''.join(res))

        # increase counters
        for i, d in enumerate(digits):
            if counters[i] >= len(digit2letters[d]) - 1:
                counters[i] = 0
            else:
                counters[i] += 1
                break
        else:
            the_end = True

    return result


def letter_combinations_recursive(digits: str) -> List[str]:
    digit2letters = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    result = []

    def iterate_and_recurse(digit_idx, path):
        if digit_idx == len(digits):
            if len(path) > 0:
                result.append(''.join(path))
            return
        for letter in digit2letters[digits[digit_idx]]:
            path.append(letter)
            iterate_and_recurse(digit_idx+1, path)
            path.pop()

    iterate_and_recurse(0, [])
    return result


def tests():
    res = letter_combinations('23')
    print(sorted(res))
    res = letter_combinations('')
    print(sorted(res))
    res = letter_combinations('2')
    print(sorted(res))


def tests_recursive():
    res = letter_combinations_recursive('23')
    print(sorted(res))
    res = letter_combinations_recursive('')
    print(sorted(res))
    res = letter_combinations_recursive('2')
    print(sorted(res))


# tests()
tests_recursive()
