"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/803/

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array
of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= start_i <= end_i <= 10^4
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        cur_interval = None
        for i in intervals:
            if cur_interval is None:
                cur_interval = i
            else:
                if i[0] <= cur_interval[1]:
                    cur_interval[1] = max(cur_interval[1], i[1])
                else:
                    result.append(cur_interval)
                    cur_interval = i
        else:
            if cur_interval is not None:
                result.append(cur_interval)

        return result


def tests():
    sol = Solution()
    res = sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    print(res)
    res = sol.merge([[1, 4], [4, 5]])
    print(res)


tests()
