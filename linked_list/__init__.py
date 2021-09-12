from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val} -> {self.next}'


def make_linked_list_from_number(n: int):
    result = ListNode()
    node = None
    for i in reversed(str(n)):
        if node is None:
            node = result
        else:
            node.next = ListNode()
            node = node.next
        node.val = int(i)
    return result


def make_linked_list_from_list(a: List[int]) -> ListNode:
    head = None
    tail = None
    for i in a:
        if head is None:
            head = ListNode(i)
            tail = head
        else:
            tail.next = ListNode(i)
            tail = tail.next

    return head
