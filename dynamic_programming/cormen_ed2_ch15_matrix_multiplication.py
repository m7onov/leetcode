"""
Задача по теме из книги Кормена. Заключается в том, чтобы найти оптимальный спосок расстановки скобок в цепочке
перемножения матриц так, чтобы общее количество скалярных умножений было минимальным
"""
import mathematics
from typing import Tuple, List


def init_matrix(rows, cols, value=None) -> List[List]:
    m: List[List] = []
    for i in range(rows):
        row = [value for _ in range(cols)]
        m.append(row)

    return m


def print_parentheses(s, i, j) -> str:
    if i == j:
        return f'A{i}'

    border = s[i][j]
    left = print_parentheses(s, i, border)
    right = print_parentheses(s, border+1, j)

    if border - i > 0:
        left = f'({left})'

    if j - border - 1 > 0:
        right = f'({right})'

    return f'{left}*{right}'


def solve(p: Tuple):
    """
    :param p: массив размерностей цепочки матрицб размера n+1, где n - количество матриц в цепочке
    :return:
    """
    n = len(p) - 1
    m: List[List] = init_matrix(n, n, None)
    s: List[List] = init_matrix(n, n, None)

    for i in range(n):
        m[i][i] = 0

    # для каждой возможной длины вычисляем стоимости всех подпоследовательностей этой длины
    for l in range(2, n + 1):
        # правая граница диапазона rm соответствует ситуации, когда rm+l-1 - это последний элемент последовательности
        for i in range(0, n - l + 1):
            j = i + l - 1
            # далее ищем такое k которое разделаяет последовательность A[i...j] оптимальным образом, то есть на 2 под-
            # последовательности A[i...k] и A[k+1...j]
            m[i][j] = mathematics.inf
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    print('\n'.join(str(i) for i in m))
    print('')
    print('\n'.join(str(i) for i in s))
    print('')
    print('Optimal cost is', m[-1])
    print('Optimal parentheses are', print_parentheses(s, 0, n-1))


# solve((10, 100, 5, 50))
# solve((5, 10, 3, 12, 5, 50, 6))
solve((30, 35, 15, 5, 10, 20, 25))
