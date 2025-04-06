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
# Bucket Sort solution - best performance!
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int] | False:
        frequency: dict[int, int] = defaultdict(int)
        for i in nums:
            frequency[i] += 1

        buckets: List[List[int]] = [[] for i in range(len(nums) + 1)]

        for num, count in frequency.items():
            buckets[count].append(num)

        ans: List[int] = []

        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                ans.append(j)
                k -= 1
                if k == 0:
                    return ans

        return False


# @leet end
