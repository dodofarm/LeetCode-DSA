from typing import List, Tuple


class MinStack_one:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = self.getMin()

        if min_val is None or val <= min_val:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min_val))

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int | None:
        return self.stack[-1] if self.stack else None


# @leet start


class MinStack:
    def __init__(self):
        self.stack: List[Tuple[int, int]] = []

    def push(self, val: int) -> None:
        if self.stack:
            min_val = min(val, self.stack[-1][1])
        else:
            min_val = val
        self.stack.append((val, min_val))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int | None:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int | None:
        return self.stack[-1][1] if self.stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @leet end
