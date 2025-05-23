# @leet start
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack: list[int] = []
        for operation in operations:
            if operation == "+":
                stack.append(stack[-1] + stack[-2])
            elif operation == "D":
                stack.append(stack[-1] * 2)
            elif operation == "C":
                stack.pop()
            else:
                stack.append(int(operation))

        return sum(stack)


# @leet end
