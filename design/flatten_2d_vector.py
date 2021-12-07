"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/112/design/811/

Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.
Implement the Vector2D class:
Vector2D(int[][] vec) initializes the object with the 2D vector vec.
next() returns the next element from the 2D vector and moves the pointer one step forward.
You may assume that all the calls to next are valid.
hasNext() returns true if there are still some elements in the vector, and false otherwise.

Example 1:
Input
["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
[[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
Output
[null, 1, 2, 3, true, true, 4, false]

Explanation
Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);
vector2D.next();    // return 1
vector2D.next();    // return 2
vector2D.next();    // return 3
vector2D.hasNext(); // return True
vector2D.hasNext(); // return True
vector2D.next();    // return 4
vector2D.hasNext(); // return False

Constraints:
0 <= vec.length <= 200
0 <= vec[i].length <= 500
-500 <= vec[i][j] <= 500
At most 10^5 calls will be made to next and hasNext.

Follow up: As an added challenge, try to code it using only iterators in C++ or iterators in Java.
"""
from typing import List


class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.i = 0
        self.j = -1
        self.nextOk = False

    def find_next(self):
        if not self.nextOk:
            self.j += 1
            while self.i < len(self.vec) and self.j >= len(self.vec[self.i]):
                self.j = 0
                self.i += 1
            self.nextOk = (self.i < len(self.vec))

    def next(self) -> int:
        self.find_next()
        self.nextOk = False
        return self.vec[self.i][self.j]

    def has_next(self) -> bool:
        self.find_next()
        return self.nextOk


class Vector2Dv2:
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.i = 0
        self.j = -1

    def find_next(self, peek=False):
        i = self.i
        j = self.j + 1
        while i < len(self.vec) and j >= len(self.vec[i]):
            j = 0
            i += 1

        if not peek:
            self.i = i
            self.j = j

        return self.vec[i][j] if i < len(self.vec) else None

    def next(self) -> int:
        return self.find_next()

    def has_next(self) -> bool:
        return self.find_next(peek=True) is not None


class Vector2Dv3:
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.i = 0
        self.j = 0

    def find_next(self, peek=False):
        while self.i < len(self.vec) and self.j >= len(self.vec[self.i]):
            self.j = 0
            self.i += 1
        return self.vec[self.i][self.j] if self.i < len(self.vec) else None

    def next(self) -> int:
        ret = self.find_next()
        self.j += 1
        return ret

    def has_next(self) -> bool:
        return self.find_next(peek=True) is not None


def tests():
    inst = Vector2Dv3([[1, 2], [3], [4]])
    print(inst.next())
    print(inst.next())
    print(inst.next())
    print(inst.has_next())
    print(inst.has_next())
    print(inst.next())
    print(inst.has_next())
    #
    inst = Vector2Dv3([[], [3]])
    print(inst.has_next())
    print(inst.next())
    print(inst.has_next())


tests()
