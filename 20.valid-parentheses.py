from typing import List


class Solution_one:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        for i in s:
            if i in ("(", "[", "{"):
                stack.append(i)
            elif not stack:
                return False
            else:
                if stack[-1] == "(" and i == ")":
                    stack.pop()
                elif stack[-1] == "[" and i == "]":
                    stack.pop()
                elif stack[-1] == "{" and i == "}":
                    stack.pop()
                else:
                    return False

        return not stack


# @leet start


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        mapping: dict[str, str] = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack: List[str] = []

        for i in s:
            if i in (")", "]", "}"):
                if len(stack) == 0 or mapping[i] != stack.pop():
                    return False
            else:
                stack.append(i)

        return bool(not stack)


# @leet end
