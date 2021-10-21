"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/805/

Given an array of meeting time intervals where intervals[i] = [start_i, end_i], return the minimum number
of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:
1 <= intervals.length <= 10^4
0 <= start_i < end_i <= 10^6
"""
from typing import List
import heapq


class Solution:
    def min_neeting_rooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        rooms_counter = 0
        heap = []
        for i in intervals:
            if len(heap) == 0:
                heapq.heappush(heap, i[1])
                rooms_counter += 1
            else:
                if i[0] < heap[0]:
                    heapq.heappush(heap, i[1])
                    rooms_counter += 1
                else:
                    heapq.heapreplace(heap, i[1])
        return rooms_counter


def tests():
    sol = Solution()
    res = sol.min_neeting_rooms([[0, 30], [5, 10], [15, 20]])
    print(res)
    res = sol.min_neeting_rooms([[7, 10], [2, 4]])
    print(res)


tests()
