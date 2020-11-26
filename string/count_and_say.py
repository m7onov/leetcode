"""
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/886/

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a
different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous
section all of the same character. Then for each group, say the number of characters, then say the character.
To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

Example 1:
Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
"""


def count_and_say(n: int) -> str:
    ls = [1]
    for i in range(n - 1):
        k = 1  # счетчик повторяющихся символов
        j = 1  # индекс следующего символа в ls
        while j < len(ls):
            if ls[j] == ls[j - 1]:
                k += 1
                ls.pop(j)
            else:
                ls.insert(j - 1, k)
                k = 1
                j += 2

        ls.insert(j - 1, k)

    return ''.join([str(i) for i in ls])
