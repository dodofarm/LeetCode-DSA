from typing import List


# @leet start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for sell in prices:
            if sell < buy:
                buy = sell

            max_profit = max(max_profit, sell - buy)

        return max_profit


# @leet end

