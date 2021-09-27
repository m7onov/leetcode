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


def generate_tests(num_tests):
    tests = []
    for _ in range(num_tests):
        can_vals = [random.randint(0, 20) for _ in range(random.randint(1, 15))]
        res_vals = list(can_vals)
        for _ in range(15):
            v = random.random()
            # interchange 2 elements
            if v < .33:
                ti1 = random.randint(0, len(res_vals)-1)
                ti2 = random.randint(0, len(res_vals)-1)
                if ti1 != ti2:
                    tv = res_vals[ti1]
                    res_vals[ti1] = res_vals[ti2]
                    res_vals[ti2] = tv
            # multiply all by something
            elif v < .66:
                tv = random.randint(-15, 15)
                if tv != 0:
                    res_vals = [i * tv for i in res_vals]
            # add something to all
            else:
                tv = random.randint(-15, 15)
                res_vals = [i + tv for i in res_vals]

        tests.append((can_vals, res_vals))

    return tests


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
            atest.can_vals.sort()
            if asc:
                atest.res_vals.sort()
            else:
                atest.res_vals.sort(reverse=True)

            if atest.res_vals[-1] == atest.res_vals[0] or atest.can_vals[-1] == atest.can_vals[0]:
                if atest.res_vals[0] == atest.can_vals[0]:
                    return True, 'trivial'
                elif atest.can_vals[0] * atest.res_vals[0] == 0:
                    if atest.can_vals[0] == atest.can_vals[-1] and atest.res_vals[0] == atest.res_vals[-1]:
                        return True, 'trivial'
                    else:
                        return False, None
                elif test.res_vals[-1] * atest.can_vals[1] == atest.res_vals[0] * atest.can_vals[-1]:
                    return True, 'trivial'
                else:
                    return False, None

            c = (atest.res_vals[-1] - atest.res_vals[0]) / (atest.can_vals[-1] - atest.can_vals[0])
            d = (atest.res_vals[0] * atest.can_vals[-1] - atest.can_vals[0] * atest.res_vals[-1]) \
                / (atest.can_vals[-1] - atest.can_vals[0])

            for can_val, res_val in zip(atest.can_vals, atest.res_vals):
                if (can_val * c + d) != res_val:
                    return False, None
            else:
                return True, f'c = {c}, d = {d}'

        for i, test in enumerate(self.tests):
            if test.can_len != test.res_len:
                self.add_solution('NO')
            elif test.can_len < 2:
                self.add_solution('YES', 'trivial')
            else:
                is_valid, details = try_solution(test, True)
                if not is_valid:
                    is_valid, details = try_solution(test, False)

                if is_valid:
                    self.add_solution('YES', details)
                else:
                    self.add_solution('NO')


# sol = Solution()
# sol.load_tests_from_file('task_b_input1.txt')
# sol.solve()
# print('\n'.join(sol.solutions))
# print('-------------------')
# sol = Solution()
# sol.load_tests_from_file('task_b_input2.txt')
# sol.solve()
# print('\n'.join(sol.solutions))
# print('-------------------')
# sol = Solution()
# sol.load_tests_from_file('task_b_input3.txt')
# sol.solve()
# print('\n'.join(sol.solutions))

while True:
    test_vals = generate_tests(1000)
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
