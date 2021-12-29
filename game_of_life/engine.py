""""
NOTE: see array/game_of_life.py
"""
import random
from typing import List, Tuple


class Board:
    def num_rows(self) -> int:
        raise NotImplementedError

    def num_cols(self) -> int:
        raise NotImplementedError

    def __getitem__(self, key):
        raise NotImplementedError

    def __setitem__(self, key, value):
        raise NotImplementedError

    def dump(self):
        raise NotImplementedError


class Engine:
    def __init__(self, board: Board, is_debug=False):
        self.board = board
        self.cache = dict()
        self.num_rows = board.num_rows()
        self.num_cols = board.num_cols()
        self.max_cache_size = 0
        self.is_debug = is_debug

    def log(self, msg):
        if self.is_debug:
            print(msg)

    def get_cell(self, row, col):
        if (row, col) in self.cache:
            entry = self.cache[row, col]
            self.log(f'({row}, {col}) reduce cache counter: {entry[1]} -> {entry[1] - 1}')
            entry[1] -= 1
            if entry[1] == 0:
                self.log(f'({row}, {col}) pop from cache')
                self.cache.pop((row, col))
            return entry[0]
        elif 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            return self.board[row, col]
        else:
            return 0

    def set_cell(self, row, col, value, read_counter):
        prev, self.board[row, col] = self.board[row, col], value
        if value != prev and read_counter > 0:
            self.log(f'({row}, {col}) add to cache: prev = {prev}, read_counter = {read_counter}')
            self.cache[row, col] = [prev, read_counter]
            self.max_cache_size = max(self.max_cache_size, len(self.cache))

    def get_new_value(self, row, col, current_value):
        num_lives = 0
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if not (i == 0 and j == 0):
                    cell_value = self.get_cell(row + i, col + j)
                    num_lives += cell_value
        if current_value == 1:
            if num_lives == 2 or num_lives == 3:
                return 1
        else:
            if num_lives == 3:
                return 1
        return 0

    def update_cell(self, row, col, read_counter):
        old_value = self.board[row, col]
        new_value = self.get_new_value(row, col, old_value)
        self.log(f'({row}, {col}) update cell: {old_value} --> {new_value}')
        self.set_cell(row, col, new_value, read_counter)

    def update_row_by_row(self):
        def get_read_counter(row, col):
            counter = 4
            if col == 0:
                counter -= 1
                if row == self.num_rows - 1:
                    counter -= 2
            elif col == self.num_cols - 1:
                counter -= 2
                if row == self.num_rows - 1:
                    counter -= 2
            elif row == self.num_rows - 1:
                counter -= 3
            return counter

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                read_counter = get_read_counter(i, j)
                self.update_cell(i, j, read_counter)

    def update_region_outwards(self, start_row, start_col):
        def get_read_counter(row, col):
            counter = 8
            if col == 0:
                counter -= 3
                if row == 0 or row == self.num_rows - 1:
                    counter -= 2
            elif col == self.num_cols - 1:
                counter -= 3
                if row == 0 or row == self.num_rows - 1:
                    counter -= 2
            elif row == 0 or row == self.num_rows - 1:
                counter -= 3
            return counter

        self.log(f'start_row = {start_row}, start_col = {start_col}')
        stop_row = start_row
        stop_col = start_col
        while start_row >= 0 or stop_row < self.num_rows or start_col >= 0 or stop_col < self.num_cols:
            if start_row == stop_row and start_col == stop_col:
                read_counter = get_read_counter(start_row, start_col)
                self.update_cell(start_row, start_col, read_counter)
            else:
                for i in range(max(start_col, 0), min(stop_col + 1, self.num_cols)):
                    if start_row >= 0:
                        read_counter = get_read_counter(start_row, i)
                        self.update_cell(start_row, i, read_counter)
                    if stop_row < self.num_rows and stop_row != start_row:
                        read_counter = get_read_counter(stop_row, i)
                        self.update_cell(stop_row, i, read_counter)
                for i in range(max(start_row + 1, 0), min(stop_row, self.num_rows)):
                    if start_col >= 0:
                        read_counter = get_read_counter(i, start_col)
                        self.update_cell(i, start_col, read_counter)
                    if stop_col < self.num_cols and stop_col != start_col:
                        read_counter = get_read_counter(i, stop_col)
                        self.update_cell(i, stop_col, read_counter)
            start_row -= 1
            start_col -= 1
            stop_row += 1
            stop_col += 1
            self.log(f'expanding: ({start_row}, {start_col}) - ({stop_row}, {stop_col})')


class MemoryBoard(Board):
    def __init__(self, board: List[List[int]]):
        self.board = board

    def num_rows(self) -> int:
        return len(self.board)

    def num_cols(self) -> int:
        return len(self.board[0])

    def dump(self):
        print('\n'.join(str(x) for x in self.board))

    def __getitem__(self, key: Tuple[int, int]) -> int:
        return self.board[key[0]][key[1]]

    def __setitem__(self, key: Tuple[int, int], value: int):
        self.board[key[0]][key[1]] = value


def test():
    cell_values = (0, 1)
    # content = [[random.choice(cell_values) for _ in range(30)] for _ in range(20)]
    # content = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    content = [
        [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]
    ]
    board = MemoryBoard(content)
    engine = Engine(board, is_debug=True)
    engine.update_region_outwards(board.num_rows() // 2, board.num_cols() // 2)
    # engine.update_row_by_row()
    board.dump()
    print(f'max_cache_size = {engine.max_cache_size}')


test()

# TODO: board from file
