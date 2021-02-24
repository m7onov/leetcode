"""
Задача по теме из книги Кормена. Заключается в том, чтобы найти оптимальный путь от начала конвеера до его конца.
При следующих условиях:

    - количество операций конвеера - n, каждая из которых может быть выполнена на одной из двух линий
    - изделие должно пройти все операции по порядку на одной из двух линий
    - времена загрузки изделия на первую и вторую линию (начальная точка) заданы - e1, e2
    - также заданы времена выполнения операций на первой и второй линии - a1[n], a2[n]
    - также заданы времена перехода между линиями на каждой операции - t1[n-1], t2[n-1]; при этом изделие может
      перейти от операции a1[i] к операции a2[i+1] за время t1[i]; аналогично со второй линии на первую
    - время перехода между операциями на одной линии равно нулю
    - также заданы времена выхода с первой и второй линий - x1, x2 до конечной точки

Требуется найти миниальное время прохождения издения от начальной точки до конечной, а также найти путь, который
соответствует этому времени.
"""
from typing import Tuple, List


def solve(e1, e2, a1, a2, t1, t2, x1, x2) -> Tuple[int, List]:
    # значение в таблице f1[i] содержит минимальное время прохождения изделия от начальной точки до позиции a1[i]
    # то же самое для таблицы f2
    f1, f2 = [], []
    # значение в таблице l1[i] содержит номер линии {1, 2} с которой изделие попало на операцию a1[i]
    # то же самое для таблицы l2
    l1, l2 = [], []

    f1.append(e1 + a1[0])
    f2.append(e2 + a2[0])

    for i in range(1, len(a1)):
        v1 = f1[i-1] + a1[i]
        v2 = f2[i-1] + t2[i-1] + a1[i]

        f1.append(min(v1, v2))
        l1.append(1 if v1 < v2 else 2)

        v1 = f1[i - 1] + t1[i - 1] + a2[i]
        v2 = f2[i-1] + a2[i]

        f2.append(min(v1, v2))
        l2.append(1 if v1 < v2 else 2)

    if f1[-1] + x1 < f2[-1] + x2:
        min_path_last_line = 1
    else:
        min_path_last_line = 2

    min_path = [min_path_last_line]
    for i in range(len(a1)-1):
        if min_path[0] == 1:
            min_path.insert(0, l1[-1-i])
        else:
            min_path.insert(0, l2[-1-i])

    return min_path_last_line, min_path


print(solve(2, 4, [7, 9, 3, 4, 8, 4], [8, 5, 6, 4, 5, 7], [2, 3, 1, 3, 4], [2, 1, 2, 2, 1], 3, 2))