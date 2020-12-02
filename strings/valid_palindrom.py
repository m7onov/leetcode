"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/883/

Given a strings, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty strings as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false

Constraints:
s consists only of printable ASCII characters.
"""


def is_palindrome(s: str) -> bool:
    ln = len(s)
    i = 0
    j = ln - 1

    dc = set([chr(k) for k in range(ord('a'), ord('z') + 1)] +
             [chr(k) for k in range(ord('A'), ord('Z') + 1)] +
             [str(k) for k in range(10)])

    ord_a, ord_A, ord_Z = ord('a'), ord('A'), ord('Z')
    while i < j:
        if s[i] not in dc:
            i += 1
            continue

        if s[j] not in dc:
            j -= 1
            continue

        c1 = s[i]
        if ord_A <= ord(c1) <= ord_Z:
            c1 = chr(ord_a + ord(c1) - ord_A)

        c2 = s[j]
        if ord_A <= ord(c2) <= ord_Z:
            c2 = chr(ord_a + ord(c2) - ord_A)

        if c1 != c2:
            return False

        i += 1
        j -= 1

    return True
