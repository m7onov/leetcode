"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/562/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
-2^31 <= val <= 2^31 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.stack_mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack_mins) == 0 or val < self.stack_mins[-1]:
            self.stack_mins.append(val)
        else:
            self.stack_mins.append(self.stack_mins[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.stack_mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.stack_mins[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.get_min())    # return -3
minStack.pop()
print(minStack.top())        # return 0
print(minStack.get_min())    # return -2
