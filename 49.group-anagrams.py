from typing import List
from collections import defaultdict


class Solution_one:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(List)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())


# Solution with sorted
class Solution_two:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans: dict[str, list[str]] = {}
        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i in ans:
                ans[sorted_i].append(i)
            else:
                ans[sorted_i] = [i]

        return list(ans.values())


# @leet start


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans: dict[tuple[int, ...], list[str]] = defaultdict(list)
        for word in strs:
            temp_list: list[int] = [0] * 26
            for letter in word:
                temp_list[ord(letter) - ord("a")] += 1
            ans[tuple(temp_list)].append(word)
        return list(ans.values())


# @leet end
