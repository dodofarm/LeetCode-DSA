from typing import List


# @leet start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []

        for i in tokens:
            tmp = i[1:] if i[0] == "-" else i
            if tmp.isnumeric():
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()

                if i == "+":
                    stack.append(b + a)

                if i == "-":
                    stack.append(b - a)

                if i == "*":
                    stack.append(b * a)
                if i == "/":
                    stack.append(int(b / a))

        return stack[0]


# @leet end
