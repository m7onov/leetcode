"""
https://contest.yandex.ru/yacup/contest/29250/problems/A/

A. Робот-секретарь (разминка)
    Ограничение времени	    1 секунда
    Ограничение памяти	    256Mb
    Ввод	                стандартный ввод или input.txt
    Вывод	                стандартный вывод или output.txt

Решение, проходящее все тесты, будет оценено в 2 балла.

Настя любит программировать и увлекается старой компьютерной техникой. Однажды она увидела в музее Яндекса робота для
набора текста на печатной машинке. Настя захотела проверить, насколько оптимально работает робот.
Клавиатура печатной машинки состоит из 26 клавиш английского алфавита, клавиши пробела и клавиши Shift, которая изменяет
регистр следующей набранной буквы на противоположный текущему. Двойное же нажатие на клавишу Shift изменяет текущий
регистр машинки. В начале работы регистр всегда нижний, то есть при наборе без клавиши Shift будут печататься строчные
буквы. Пробел одинаково набирается в обоих регистрах.

Настя хочет понять, за какое минимальное количество нажатий можно набрать текст, чтобы сравнить это с результатами
робота.

Это разминочная задача, к которой мы размещаем готовое решения, чтобы вы могли познакомиться с нашей автоматической
системой проверки решений. Ввод и вывод осуществляется через файлы, либо через стандартные потоки ввода-вывода,
как вам удобнее.

Пример решения на С++: https://pastebin.com/gUv33Cd9. В качестве компилятора выбирайте GNU C++ 14 4.9.

Формат ввода
Входные данные – строка
s (1 ≤ |s| ≤ 100000), состоящая из прописных и строчных букв английского алфавита, а также символа пробела.

Формат вывода
Выведите единственное число — минимальное количество нажатий, необходимое, чтобы напечатать данную строку.

Пример 1
Ввод	        Вывод
Hello World     13

Пример 2
Ввод	        Вывод
APPLE II        10
"""
import sys


def solution(s):
    def if_lowercase(c, y, n, s):
        if 'a' <= c <= 'z':
            return y
        elif 'A' <= c <= 'Z':
            return n
        else:
            return s

    small = [0] * (len(s) + 1)
    big = [0] * (len(s) + 1)

    for i, c in enumerate(s, 1):
        small[i] = min(small[i-1] + if_lowercase(c, 1, 2, 1),
                       big[i-1] + if_lowercase(c, 3, 3, 3) if i > 1 else sys.maxsize)

        big[i] = min(small[i-1] + if_lowercase(c, 3, 3, 3),
                     big[i-1] + if_lowercase(c, 2, 1, 1) if i > 1 else sys.maxsize)

    return min(small[-1], big[-1])


# with open('input.txt') as f:
#     in_str = f.read().strip('\n')  # !!! strip('\n') - это блять очень важно; 2 дня убил на это !!!
#
# res = solution(in_str)
# print(res)

print(solution('Hello World'))
print(solution('APPLE II'))
