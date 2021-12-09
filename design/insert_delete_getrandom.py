"""
https://leetcode.com/explore/interview/card/top-interview-questions-medium/112/design/813/

Implement the RandomizedSet class:
    - RandomizedSet() Initializes the RandomizedSet object.
    - bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present,
        false otherwise.
    - bool remove(int val) Removes an item val from the set if present. Returns true if the item was present,
        false otherwise.
    - int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one
        element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

Constraints:
-2^31 <= val <= 2^31 - 1
At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""
import random
from collections import defaultdict


class RandomizedSet:

    def __init__(self):
        self.a = []
        self.s = dict()

    def insert(self, val: int) -> bool:
        not_exists = val not in self.s
        if not_exists:
            idx = len(self.a)
            self.a.append(val)
            self.s[val] = idx
        return not_exists

    def remove(self, val: int) -> bool:
        exists = val in self.s
        if exists:
            idx = self.s[val]
            self.a[idx] = self.a[-1]
            self.s[self.a[idx]] = idx
            del self.a[-1]  # is it really O(1) ?
            del self.s[val]

        return exists

    def get_random(self) -> int:
        idx = random.randint(0, len(self.a) - 1)
        return self.a[idx]


class RandomizedSet2:

    def __init__(self):
        self.a = []
        self.s = dict()
        self.e = -1

    def insert(self, val: int) -> bool:
        not_exists = val not in self.s
        if not_exists:
            self.e += 1
            self.s[val] = self.e
            if self.e == len(self.a):
                self.a.append(val)
            else:
                self.a[self.e] = val

        print(f'insert: val = {val}, a = {self.a}, s = {self.s}, e = {self.e}')
        return not_exists

    def remove(self, val: int) -> bool:
        exists = val in self.s
        if exists:
            idx = self.s[val]
            self.a[idx] = self.a[self.e]
            self.s[self.a[idx]] = idx
            self.e -= 1
            del self.s[val]

        print(f'remove: val = {val}, a = {self.a}, s = {self.s}, e = {self.e}')
        return exists

    def get_random(self) -> int:
        idx = random.randint(0, self.e)
        print(f'random: a = {self.a}, s = {self.s}, e = {self.e}')
        return self.a[idx]


def tests():
    rs = RandomizedSet2()
    rs.insert(3)
    rs.insert(-2)
    rs.remove(2)
    rs.insert(1)
    rs.insert(-3)
    rs.insert(-2)
    rs.remove(-2)
    rs.remove(3)
    rs.insert(-1)
    rs.remove(-3)
    rs.insert(1)
    rs.insert(-2)
    rs.insert(-2)
    rs.insert(-2)
    rs.insert(1)
    res = rs.get_random()
    print(f'-2 = {res}')
    rs.insert(-2)
    rs.remove(0)
    rs.insert(-3)
    rs.insert(1)

    # test uniformity
    for i in range(100):
        j = random.randint(0, 30)
        c = random.randint(0, 2)
        if c == 0:
            rs.insert(j)
        elif c == 1:
            rs.remove(j)
        elif len(rs.a) > 0:
            dist = defaultdict(int)
            for k in range(1000):
                n = rs.get_random()
                dist[n] += 1
            print(dist.values())


tests()
