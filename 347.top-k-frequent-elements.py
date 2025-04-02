from collections import defaultdict
from typing import List


# @leet start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans: dict[int, int] = defaultdict(int)
        for i in nums:
            ans[i] += 1

        res = []
        values = sorted(ans.items(), key=lambda x: x[1])
        for i in range(0, k):
            res.append(values.pop()[0])

        return res


# @leet end
