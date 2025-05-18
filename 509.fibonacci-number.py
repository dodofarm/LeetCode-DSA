from functools import cache


class Solution_one:
    def fib(self, n: int) -> int:
        prev = 0
        ans = 1

        for _ in range(n):
            ans, prev = ans + prev, ans

        return prev


# @leet start


class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


# @leet end
