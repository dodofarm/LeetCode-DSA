# Nonoptimal solution
class Solution_one:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            while start < end:
                if s[start].lower().isalnum():
                    break
                start += 1
            while end > start:
                if s[end].lower().isalnum():
                    break
                end -= 1
            if s[start].lower() != s[end].lower():
                if not s[start].isalnum() or not s[end].isalnum():
                    return True
                return False

            start += 1
            end -= 1

        return True


# @leet start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s) - 1

        while p1 < p2:
            if not s[p1].isalnum():
                p1 += 1
                continue
            if not s[p2].isalnum():
                p2 -= 1
                continue

            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1

        return True


# @leet end
