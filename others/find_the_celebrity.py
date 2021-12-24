"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/825/

Suppose you are at a party with n people (labeled from 0 to n - 1), and among them, there may exist one celebrity.
The definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is
to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out
the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int
findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if
there is a celebrity in the party. If there is no celebrity, return -1.

Example 1:

.. image:: https://assets.leetcode.com/uploads/2019/02/02/277_example_1_bold.PNG

Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j,
otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because
both 0 and 2 know him but 1 does not know anybody.

Example 2:

.. image:: https://assets.leetcode.com/uploads/2019/02/02/277_example_2.PNG

Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.

Constraints:
n == graph.length
n == graph[i].length
2 <= n <= 100
graph[i][j] is 0 or 1.
graph[i][i] == 1

Follow up: If the maximum number of allowed calls to the API knows is 3 * n, could you find a solution
without exceeding the maximum number of calls?
"""
import random
from collections import defaultdict


# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


def generate_graph(n, has_celebrity=True):
    graph = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
    celebrity_idx = None
    if has_celebrity:
        celebrity_idx = random.randint(0, n - 1)
        for row in range(n):
            for col in range(n):
                if row == celebrity_idx:
                    graph[row][col] = 0
                if col == celebrity_idx:
                    graph[row][col] = 1

    celebrity_cols = set([i for i in range(n)])
    celebrity_rows = set([i for i in range(n)])
    for row in range(n):
        for col in range(n):
            if graph[row][col] == 1 and row != col:
                celebrity_rows.discard(row)
            if graph[row][col] == 0:
                celebrity_cols.discard(col)

    for celebrity_row in celebrity_rows:
        if celebrity_row != celebrity_idx:
            set_col_idx = random.randint(0, n - 1)
            if set_col_idx >= celebrity_row:
                set_col_idx += 1
            graph[celebrity_row][set_col_idx] = 1

    for i in range(n):
        graph[i][i] = 1

    return graph, celebrity_idx


class Solution:
    def __init__(self, graph):
        self.graph = graph
        self.knows_counter = 0

    def knows(self, a: int, b: int):
        self.knows_counter += 1
        return self.graph[a][b] == 1

    def find_celebrity_1(self, n: int) -> int:
        def shrink_candidates(candidates: set):
            base_candidate = None
            exclude_candidates = set()
            for j in candidates:
                if base_candidate is None:
                    base_candidate = j
                else:
                    if not self.knows(base_candidate, j) or self.knows(j, base_candidate):
                        exclude_candidates.add(j)
            if len(exclude_candidates) == 0:
                candidates.discard(base_candidate)
                return candidates
            else:
                return candidates - exclude_candidates

        celeb_candidates = set(i for i in range(n))
        print(f'celeb_candidates = {celeb_candidates}, knows_counter = {self.knows_counter}')
        while len(celeb_candidates) > 1:
            celeb_candidates = shrink_candidates(celeb_candidates)
            print(f'celeb_candidates = {celeb_candidates}, knows_counter = {self.knows_counter}')

        final_candidate = celeb_candidates.pop()
        for i in range(n):
            if i != final_candidate:
                if self.knows(final_candidate, i) or not self.knows(i, final_candidate):
                    return -1

        print(f'celeb_candidates = {celeb_candidates}, knows_counter = {self.knows_counter}')
        return final_candidate

    def find_celebrity_2(self, n: int) -> int:
        cache = dict()

        def x_knows(a, b) -> bool:
            if (a, b) not in cache:
                cache[a, b] = self.knows(a, b) == 1
            return cache[a, b]

        def shrink_candidates(candidates: set):
            exclude_candidates = set()
            base_candidate = next(iter(candidates))
            for j in candidates.difference({base_candidate}):
                if not x_knows(base_candidate, j):
                    exclude_candidates.add(j)
                else:
                    return candidates - exclude_candidates - {base_candidate}
            return candidates - exclude_candidates

        celeb_candidates = set(i for i in range(n))
        # print(f'celeb_candidates = {celeb_candidates}, knows_counter = {self.knows_counter}')
        while len(celeb_candidates) > 1:
            celeb_candidates = shrink_candidates(celeb_candidates)
            # print(f'celeb_candidates = {celeb_candidates}, knows_counter = {self.knows_counter}')

        final_candidate = celeb_candidates.pop()
        for i in range(n):
            if i != final_candidate:
                if not x_knows(i, final_candidate) or x_knows(final_candidate, i):
                    return -1

        # print(f'celeb_candidates = {celeb_candidates}, knows_counter = {self.knows_counter}')
        return final_candidate

    def find_celebrity_3(self, n: int) -> int:
        cache = dict()

        def x_knows(a, b) -> bool:
            if (a, b) not in cache:
                cache[a, b] = self.knows(a, b) == 1
            return cache[a, b]

        suspect = 0
        for i in range(1, n):
            if x_knows(suspect, i):
                suspect = i

        for i in range(n):
            if i != suspect:
                if not x_knows(i, suspect) or x_knows(suspect, i):
                    return -1

        return suspect


def test():
    celebrity_idx = 14
    graph = [
        [1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
        [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
        [1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
        [0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
        [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1]
    ]
    sol = Solution(graph)
    res = sol.find_celebrity_3(len(graph))
    if res != celebrity_idx:
        print(f'wrong answer: {res} != {celebrity_idx}')
    print(f'Good answer: {res} == {celebrity_idx}')
    return sol.knows_counter


def random_test():
    graph, celebrity_idx = generate_graph(100)
    sol = Solution(graph)
    res = sol.find_celebrity_2(len(graph))
    if res != celebrity_idx:
        print(f'wrong answer: {res} != {celebrity_idx}')
        print('\n'.join([str(row) for row in graph]))
        raise Exception('error')
    return sol.knows_counter


def run_random_tests():
    num_counters = 0
    max_counter = 0
    sum_counter = 0
    for _ in range(1000):
        counter = random_test()
        if counter > max_counter:
            max_counter = counter
        sum_counter += counter
        num_counters += 1
    print(f'max_counter = {max_counter}')
    print(f'avg_counter = {sum_counter / num_counters}')


run_random_tests()
# test()
