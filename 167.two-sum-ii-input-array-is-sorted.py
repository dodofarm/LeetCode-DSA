from typing import List


# @leet start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            ans = target - numbers[end]
            if numbers[start] < ans:
                start += 1
            elif numbers[start] > ans:
                end -= 1
            else:
                return [start + 1, end + 1]
        return [0, 0]


# @leet end
