"""
https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

You are given a string s.
A split is called good if you can split s into two non-empty strings s_left and s_right where their concatenation
is equal to s (i.e., s_left + s_right = s) and the number of distinct letters in s_left and s_right is the same.

Return the number of good splits you can make in s.

Example 1:
    Input: s = "aacaba"
    Output: 2
    Explanation:
        There are 5 ways to split "aacaba" and 2 of them are good.
            ("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
            ("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
            ("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
            ("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
            ("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.

Example 2:
    Input: s = "abcd"
    Output: 1
    Explanation: Split the string as follows ("ab", "cd").

Constraints:
    1 <= s.length <= 10^5
    s consists of only lowercase English letters.
"""


class Solution:
    def num_splits(self, s: str) -> int:
        sl = len(s)
        ls = set()
        rs = set()
        la = list()
        ra = list()
        for li in range(sl):
            if s[li] not in ls:
                la.append(li)
                ls.add(s[li])

            ri = sl - 1 - li
            if s[ri] not in rs:
                ra.insert(0, ri)
                rs.add(s[ri])

        num_splits = 0
        ld_pointer = 0
        rd_pointer = 0
        for li in range(sl):
            if ld_pointer < len(la) and li >= la[ld_pointer]:
                ld_pointer += 1

            if rd_pointer < len(ra) and li >= ra[rd_pointer]:
                rd_pointer += 1

            print(f"{li}: {ld_pointer} - {len(ra) - rd_pointer}")
            if ld_pointer == len(ra) - rd_pointer:
                num_splits += 1
            elif ld_pointer > len(ra) - rd_pointer:
                break

        return num_splits


def test1():
    sol = Solution()
    ans = sol.num_splits('aacaba')
    print(ans)
    ans = sol.num_splits('abcd')
    print(ans)


test1()
