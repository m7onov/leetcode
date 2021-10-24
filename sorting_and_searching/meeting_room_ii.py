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
    def min_meeting_rooms(self, intervals: List[List[int]]) -> int:
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

    def min_meeting_rooms2(self, intervals: List[List[int]]) -> int:
        beginings = sorted(map(lambda x: x[0], intervals))
        endinds = sorted(map(lambda x: x[1], intervals))
        min_rooms, counter = 0, 0
        cur_b_i, cur_e_i = 0, 0
        while cur_b_i < len(beginings):
            while beginings[cur_b_i] >= endinds[cur_e_i]:
                cur_e_i += 1
                counter -= 1
            counter += 1
            cur_b_i += 1
            min_rooms = max(min_rooms, counter)

        return min_rooms


def tests():
    sol = Solution()
    res = sol.min_meeting_rooms2([[0, 30], [5, 10], [15, 20]])
    print(f'2 = {res}')
    res = sol.min_meeting_rooms2([[7, 10], [2, 4]])
    print(f'1 = {res}')
    res = sol.min_meeting_rooms2([[1293, 2986], [848, 3846], [4284, 5907], [4466, 4781], [518, 2918], [300, 5870]])
    print(f'4 = {res}')
    res = sol.min_meeting_rooms2([[2, 7]])
    print(f'1 = {res}')


tests()
