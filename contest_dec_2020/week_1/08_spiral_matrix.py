"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3557/

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
"""
from typing import List


def generate_matrix_dumb(n: int) -> List[List[int]]:
    ret_list = [[0 for _ in range(n)] for _ in range(n)]
    start_val = 1
    r = 0
    side_len = n - 2*r
    while side_len > 1:
        for k in range(4 * side_len - 4):
            v = start_val + k
            if (start_val + 0*(side_len - 1)) <= v <= (start_val + 1*(side_len - 1) - 1):
                i = r
                j = r + k

            elif (start_val + 1*(side_len - 1)) <= v <= (start_val + 2*(side_len - 1) - 1):
                j = r + side_len - 1
                i = r + k - (side_len - 1)

            elif (start_val + 2*(side_len - 1)) <= v <= (start_val + 3*(side_len - 1) - 1):
                i = r + side_len - 1
                j = r + side_len - (k + 1 - 2*(side_len - 1))

            elif (start_val + 3*(side_len - 1)) <= v <= (start_val + 4*(side_len - 1) - 1):
                j = r
                i = r + side_len - (k + 1 - 3*(side_len - 1))

            else:
                raise Exception('unexpected: ', start_val, side_len, v)

            ret_list[i][j] = v

        start_val += 4 * side_len - 4
        r += 1
        side_len = n - 2*r

    if side_len == 1:
        ret_list[n//2][n//2] = start_val

    return ret_list


def generate_matrix_smart(n: int) -> List[List[int]]:
    ret_list = [[0 for _ in range(n)] for _ in range(n)]
    counter = 1
    num_layers = (n + 1) // 2
    for layer in range(num_layers):
        for i in range(n - 2 * layer):
            ret_list[layer][layer + i] = counter
            counter += 1

        for i in range(1, n - 2 * layer):
            ret_list[layer + i][n - 1 - layer] = counter
            counter += 1

        for i in range(1, n - 2 * layer):
            ret_list[n - 1 - layer][n - 1 - layer - i] = counter
            counter += 1

        for i in range(1, n - 2 * layer - 1):
            ret_list[n - 1 - layer - i][layer] = counter
            counter += 1

    return ret_list


def generate_matrix_smarter(n: int) -> List[List[int]]:
    ret_list = [[0 for _ in range(n)] for _ in range(n)]
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    row, col, dr = 0, 0, 0
    for counter in range(1, n*n+1):
        ret_list[row][col] = counter
        if ret_list[(row + dirs[dr][0]) % n][(col + dirs[dr][1]) % n] != 0:
            dr = (dr + 1) % 4

        row += dirs[dr][0]
        col += dirs[dr][1]

    return ret_list


# print('\n'.join([str(i) for i in generate_matrix_smart(1)]))
# print('\n'.join([str(i) for i in generate_matrix_smart(5)]))
# print('\n'.join([str(i) for i in generate_matrix_smarter(1)]))
# print('\n'.join([str(i) for i in generate_matrix_smarter(5)]))
