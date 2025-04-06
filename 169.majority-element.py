from typing import List
from collections import defaultdict
import heapq


# O(n) space complexity also the popping from the heap is not O(n)
class Solution_one:
    def majorityElement(self, nums: List[int]) -> int:
        frequency: dict[int, int] = defaultdict(int)
        for i in nums:
            frequency[i] += 1
        freq = [(-a, b) for b, a in frequency.items()]
        heapq.heapify(freq)
        return heapq.heappop(freq)[1]


# Simpler Solution but still creates a dict with all values in the array as keys
class Solution_two:
    def majorityElement(self, nums: List[int]) -> int:
        count: dict[int, int] = defaultdict(int)
        majority = 0
        for i in nums:
            count[i] += 1
            if count[i] > count[majority]:
                majority = i
        print(majority)
        print(count)

        return majority


# @leet start


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        ans = 0
        for i in nums:
            if majority == 0:
                ans = i
            majority += 1 if ans == i else -1

        return ans


# @leet end

