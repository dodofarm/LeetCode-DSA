from collections import defaultdict
from typing import List
import heapq


# Sorting first solution
class Solution_one:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans: dict[int, int] = defaultdict(int)
        for i in nums:
            ans[i] += 1

        res = []
        values = sorted(ans.items(), key=lambda x: x[1])
        for i in range(0, k):
            res.append(values.pop()[0])

        return res


# heapify solution
class Solution_two:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: dict[int, int] = defaultdict(int)
        for i in nums:
            count[i] += 1

        arr = [(-b, a) for a, b in count.items()]
        heapq.heapify(arr)
        ans = []
        for i in range(0, k):
            ans.append(heapq.heappop(arr)[1])

        return ans


# @leet start

# class Solution:
#     def topKFrequent

# @leet end
