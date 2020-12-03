"""
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3552/

Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability
of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without
using extra space?

Example:
// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
"""
import random
from typing import List


class ListNode:
    def __init__(self, val=0, nx=None):
        self.val = val
        self.next = nx

    def __str__(self):
        return str(self.val) + '->' + str(self.next)


class SolutionDump:

    # NOTE: как доказать равновероятность или близкое к этому поведение???
    # нужно исследовать зависимость распределения от начального значения upper_bound

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.node = head
        self.list_idx = 0
        self.list_len = None

    def get_random(self) -> int:
        """
        Returns a random node's value.
        """
        if self.list_len is None:
            upper_bound = 1000
        else:
            upper_bound = self.list_len

        for i in range(random.randint(1, upper_bound)):
            if self.list_len is None:
                if self.node.next is None:
                    self.list_len = self.list_idx + 1
                else:
                    self.list_idx += 1

            if self.node.next is None:
                self.node = self.head
            else:
                self.node = self.node.next

        return self.node.val


class SolutionReservoirSampling:

    def __init__(self, head: ListNode):
        self.head = head

    def get_random_sample(self, sample_size: int = 1) -> List:
        reservoir = []
        i = 0
        node = self.head

        while i < sample_size and node is not None:
            reservoir.append(node.val)
            node = node.next
            i += 1

        while node is not None:
            j = random.randint(0, i)
            if j < sample_size:
                reservoir[j] = node.val

            node = node.next
            i += 1

        return reservoir

    def get_random(self) -> int:
        return self.get_random_sample(1)[0]


def init_list():
    lst = [i for i in range(300)]
    root = node = ListNode(0)
    for i in lst:
        node.next = ListNode(i)
        node = node.next
    return root


_root = init_list()
print(SolutionReservoirSampling(_root).get_random_sample(10))
