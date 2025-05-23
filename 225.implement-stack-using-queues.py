from collections import deque


# @leet start
class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.appendleft(x)
        for _ in range(len(self.queue) - 1):
            val = self.queue.pop()
            self.queue.appendleft(val)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not bool(self.queue)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @leet end
