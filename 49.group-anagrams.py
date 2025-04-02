from typing import List
from collections import defaultdict


# @leet start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(List)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())


# @leet end
# res = defaultdict(list)
# for s in strs:
#     count: list[int] = [0] * 26
#     for c in s:
#         count[ord(c) - ord("a")] += 1
#     res[tuple(count)].append(s)
# return list(res.values())
