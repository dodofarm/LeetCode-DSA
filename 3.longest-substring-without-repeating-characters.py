class Solution_one:
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


# @leet start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1, p2, ans = 0, 0, 0
        unique_vals: set[str] = set()

        while p2 < len(s):
            while s[p2] in unique_vals:
                unique_vals.remove(s[p1])
                p1 += 1
            unique_vals.add(s[p2])
            p2 += 1
            ans = max(ans, len(unique_vals))

        return ans


# @leet end
