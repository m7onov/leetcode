"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/826/

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task.
Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete
either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

Constraints:
1 <= task.length <= 10^4
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
"""
import heapq
from collections import Counter
from typing import List


class Solution:
    def least_interval_1(self, tasks: List[str], n: int) -> int:
        print(Counter(tasks))
        path = []
        tasks_heap = [i for i in map(lambda x: (-x[1], x[0]), Counter(tasks).items())]
        heapq.heapify(tasks_heap)
        hot_tasks = []
        heapq.heapify(hot_tasks)
        while len(tasks_heap) > 0 or len(hot_tasks) > 0:
            if len(tasks_heap) > 0:
                counter, task = heapq.heappop(tasks_heap)
                counter += 1
                if counter < 0:
                    heapq.heappush(hot_tasks, (len(path), task, counter))
                path.append(task)

            else:
                path.append('-')

            while len(hot_tasks) > 0 and len(path) > hot_tasks[0][0] + n:
                _, task, counter = heapq.heappop(hot_tasks)
                heapq.heappush(tasks_heap, (counter, task))

        print(path)
        return len(path)

    def least_interval_2(self, tasks: List[str], n: int) -> int:
        tasks_counter = Counter(tasks)
        print(tasks_counter)
        tasks_counter = sorted(tasks_counter.values(), reverse=True)
        num_idles = (tasks_counter[0] - 1) * n

        for task_counter in tasks_counter[1:]:
            num_idles -= min(tasks_counter[0] - 1, task_counter)

        if num_idles <= 0:
            return len(tasks)
        else:
            return len(tasks) + num_idles


def tests():
    sol = Solution()
    res = sol.least_interval_2(['A', 'A', 'A', 'B', 'B', 'B'], 2)
    print(res)
    res = sol.least_interval_2(['A', 'A', 'A', 'B', 'B', 'B'], 0)
    print(res)
    res = sol.least_interval_2(['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'], 2)
    print(res)


tests()


