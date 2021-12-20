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


# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


def generate_graph(n, has_celebrity=True):
    graph = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
    celebrity_idx = None
    if has_celebrity:
        celebrity_idx = random.randint(0, n)
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

    def knows(self, a: int, b: int):
        return self.graph[a][b] == 1

    def find_celebrity(self, n: int) -> int:
        pass


def tests():
    graph, celebrity_idx = generate_graph(10)
    print('\n'.join([str(row) for row in graph]))
    print(f'celebrity_idx = {celebrity_idx}')
    sol = Solution(graph)
    res = sol.find_celebrity(10)
    print(res)


tests()
