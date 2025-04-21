import math


# @leet start
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        p1, p2 = 1, max(piles)
        res = 0

        while p1 <= p2:
            k = (p1 + p2) // 2
            time = h
            for pile in piles:
                time -= math.ceil(pile / k)
                if time < 0:
                    break

            if time < 0:
                p1 = k + 1
            else:
                p2 = k - 1
                res = k

        return res


# @leet end
