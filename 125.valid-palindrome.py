# Nonoptimal solution - try again!
# @leet start
class Solution:
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


# @leet end
