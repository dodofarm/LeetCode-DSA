from typing import List


# same solution but didn't think of using just max_value here and calculated avg on every step
class Solution_one:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tmp_val = 0
        for i in range(k):
            tmp_val += nums[i]

        max_average = tmp_val / k

        for i in range(k, len(nums)):
            tmp_val -= nums[i - k]
            tmp_val += nums[i]
            average = tmp_val / k
            max_average = max(max_average, average)

        return max_average


# @leet start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tmp_val = 0
        for i in range(k):
            tmp_val += nums[i]

        max_value = tmp_val

        for i in range(k, len(nums)):
            tmp_val -= nums[i - k]
            tmp_val += nums[i]
            max_value = max(max_value, tmp_val)

        return max_value / k


# @leet end
