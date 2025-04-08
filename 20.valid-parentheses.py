from typing import List


# @leet start
class Solution:
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


# @leet end
