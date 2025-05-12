# @leet start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in s:
            count[ord(i) - ord("a")] += 1

        for i in t:
            index = ord(i) - ord("a")
            if count[index] > 0:
                count[index] -= 1
            else:
                return False
        return True


# @leet end
