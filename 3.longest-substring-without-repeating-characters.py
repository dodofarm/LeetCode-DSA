# @leet start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        max_length = 0
        vals: set[str] = set()
        for p2 in range(len(s)):
            while s[p2] in vals:
                vals.remove(s[p1])
                p1 += 1
            vals.add(s[p2])
            max_length = max(max_length, len(vals))

        return max_length


# @leet end
