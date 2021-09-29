"""
https://contest.yandex.ru/yacup/contest/29250/problems/B/

B. Тестирование функции (разминка)
    Ограничение времени	3 секунды
    Ограничение памяти	256Mb
    Ввод	стандартный ввод или input.txt
    Вывод	стандартный вывод или output.txt

Решение, проходящее все тесты первой группы, будет оценено в 1 балл.
Решение, проходящее все тесты, будет оценено в 3 балла, т.е. в 2 дополнительных балла.

Чтобы написать тест, нужно проверить результат работы функции, которая возвращает массив. Известен канонический
результат, однако функция не обязана выдавать в точности его. Результат функции правильный, если он может быть получен
из канонического выполнением любого числа, возможно нулевого, следующих операций:
    1. Переставить любые два элемента массива.
    2. Добавить ко всем элементам массива одно и то же число.
    3. Умножить все элементы массива на одно и то же ненулевое число.

Определите, правильный ли результат работы функции.
Это разминочная задача, к которой мы размещаем готовое решения, чтобы вы могли познакомиться с нашей автоматической
системой проверки решений. Ввод и вывод осуществляется через файлы, либо через стандартные потоки ввода-вывода,
как вам удобнее.
Пример решения на С++: https://pastebin.com/aBLx9RNK. . В качестве компилятора выбирайте GNU C++ 14 4.9.

Формат ввода
В первой строке задано число тестов
T (1 ≤ T ≤ 1000). В следующих строках идут описания T тестов.
В первой строке теста задана длина N (0 ≤ N ≤ 100000) канонического результата. В следующей строке заданы
N элементов канонического результата a_i (−1000000000 ≤ a_i ≤ 1000000000). За ними в следующей строке задана длина
M (0 ≤ M ≤ 100000) результата функции. После чего в следующей строке заданы M элементов результата функции
b_i (−1000000000 ≤ b_i ≤ 1000000000).
Суммарный размер длин всех массивов не превосходит 1000000.
Все числа целые.

Формат вывода
Для каждого из T тестов выведите на отдельной строке YES, если функция вернула правильный результат,
и NO в противном случае.
"""
import random
from collections import namedtuple


Test = namedtuple('Test', ['can_len', 'can_vals', 'res_len', 'res_vals'])


def parse_test(line_idx, input_lines):
    can_len = int(input_lines[line_idx])
    line_idx += 1
    can_vals = [int(e) for e in input_lines[line_idx].split()]
    line_idx += 1
    res_len = int(input_lines[line_idx])
    line_idx += 1
    res_vals = [int(e) for e in input_lines[line_idx].split()]
    line_idx += 1
    return line_idx, Test(can_len, can_vals, res_len, res_vals)


class Solution:
    def __init__(self):
        self.tests = []
        self.solutions = []
        self.solutions_detail = []

    def load_tests_from_file(self, filename):
        with open(filename) as f:
            input_lines = [line.strip() for line in f.readlines()]

        num_tests = int(input_lines[0])
        self.tests = []

        line_idx = 1
        for i in range(1, num_tests+1):
            line_idx, test = parse_test(line_idx, input_lines)
            self.tests.append(test)

    def load_tests(self, vals):
        for can_vals, res_vals in vals:
            self.tests.append(Test(len(can_vals), can_vals, len(res_vals), res_vals))

    def add_solution(self, asol, adetails=None):
        self.solutions.append(asol)
        self.solutions_detail.append(adetails)

    def solve(self):
        def try_solution(atest, asc=True):
            # can_vals = sorted(atest.can_vals)
            # if asc:
            #     res_vals = sorted(atest.res_vals)
            # else:
            #     res_vals = sorted(atest.res_vals, reverse=True)

            can_vals = sorted(atest.can_vals)
            res_vals = sorted(atest.res_vals)
            if not asc:
                can_vals = [-cv for cv in reversed(can_vals)]

            # if res_vals[-1] == res_vals[0] or can_vals[-1] == can_vals[0]:
            #     if res_vals[0] == can_vals[0]:
            #         return True, 'trivial'
            #     elif can_vals[0] * res_vals[0] == 0:
            #         if can_vals[0] == can_vals[-1] and res_vals[0] == res_vals[-1]:
            #             return True, 'trivial'
            #         else:
            #             return False, None
            #     elif res_vals[-1] * can_vals[1] == res_vals[0] * can_vals[-1]:
            #         return True, 'trivial'
            #     else:
            #         return False, None

            if can_vals[-1] == can_vals[0]:
                if res_vals[-1] == res_vals[-1]:
                    return True, 'trivial'
                else:
                    return False, None
            elif res_vals[-1] == res_vals[0]:
                return False, None

            # v1 = res_vals[-1] - res_vals[0]
            # v2 = can_vals[-1] - can_vals[0]
            # v3 = res_vals[0] * can_vals[-1] - can_vals[0] * res_vals[-1]

            # for can_val, res_val in zip(can_vals, res_vals):
            #     if can_val * v1 + v3 != res_val * v2:
            #         return False, None
            # else:
            #     return True, f'v1 = {v1}, v2 = {v2}, v3 = {v3}'

            diff_can = can_vals[-1] - can_vals[0]
            diff_res = res_vals[-1] - res_vals[0]
            for can_val, res_val in zip(can_vals, res_vals):
                if (can_val - can_vals[0]) * diff_res != (res_val - res_vals[0]) * diff_can:
                    return False, None
            return True, None

        for i, test in enumerate(self.tests):
            if test.can_len != test.res_len:
                self.add_solution('NO')
            elif test.can_len < 2:
                self.add_solution('YES', 'trivial')
            else:

                # ----->>
                can_vals = sorted(test.can_vals)
                res_vals = sorted(test.res_vals)
                if can_vals[0] == can_vals[-1]:
                    if res_vals[0] == res_vals[-1]:
                        self.add_solution('YES')
                    else:
                        self.add_solution('NO')
                elif res_vals[0] == res_vals[-1]:
                    self.add_solution('NO')
                else:
                    def check(a, b):
                        diff_a = a[-1] - a[0]
                        diff_b = b[-1] - b[0]
                        for i, j in zip(a, b):
                            if (i - a[0]) * diff_b != (j - b[0]) * diff_a:
                                return False
                        return True

                    can_vals_neg = [-i for i in reversed(can_vals)]
                    if check(can_vals, res_vals) or check(can_vals_neg, res_vals):
                        self.add_solution('YES')
                    else:
                        self.add_solution('NO')
                # <<-----

                # is_valid, details = try_solution(test, True)
                # if not is_valid:
                #     is_valid, details = try_solution(test, False)
                #
                # if is_valid:
                #     self.add_solution('YES', details)
                # else:
                #     self.add_solution('NO')


def release_tests():
    sol = Solution()
    sol.load_tests_from_file('task_b_input1.txt')
    sol.solve()
    print('\n'.join(sol.solutions))
    print('-------------------')
    sol = Solution()
    sol.load_tests_from_file('task_b_input2.txt')
    sol.solve()
    print('\n'.join(sol.solutions))
    print('-------------------')
    sol = Solution()
    sol.load_tests_from_file('task_b_input3.txt')
    sol.solve()
    print('\n'.join(sol.solutions))


def release():
    sol = Solution()
    sol.load_tests_from_file('input.txt')
    sol.solve()
    print('\n'.join(sol.solutions))


def random_tests():
    def generate_tests(num_tests):
        tests = []
        for _ in range(num_tests):
            can_vals = [random.randint(-5, 5) for _ in range(random.randint(1, 5))]
            res_vals = list(can_vals)
            for _ in range(20):
                v = random.random()
                if v < .33:
                    ti1 = random.randint(0, len(res_vals) - 1)
                    ti2 = random.randint(0, len(res_vals) - 1)
                    if ti1 != ti2:
                        tv = res_vals[ti1]
                        res_vals[ti1] = res_vals[ti2]
                        res_vals[ti2] = tv
                elif v < .66:
                    tv = random.randint(0, 1000)
                    if tv != 0:
                        res_vals = [i * tv for i in res_vals]
                else:
                    tv = 10 * random.randint(0, 1000)
                    res_vals = [i + tv for i in res_vals]
            tests.append((can_vals, res_vals))
        return tests

    while True:
        test_vals = generate_tests(10)
        sol = Solution()
        sol.load_tests(test_vals)
        sol.solve()
        is_found = False
        for test, solution, details in zip(sol.tests, sol.solutions, sol.solutions_detail):
            if solution != 'YES':
                print(f'{solution: <4}: {test} [{details}]')
                is_found = True

        if is_found:
            break


def specific_tests():
    sol = Solution()
    sol.load_tests([([-1, 2, 2], [6231453.859508636, 6231453.859508636, 3463540.880245016])])
    sol.solve()
    print('\n'.join(sol.solutions))


# random_tests()
# specific_tests()
release_tests()
# release()
