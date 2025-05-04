# @leet start
class Solution:
    def romanToInt(self, s: str) -> int:
        mapping: dict[str, int] = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }
        ans = 0
        for index in range(len(s) - 1):
            if mapping[s[index]] < mapping[s[index + 1]]:
                ans -= mapping[s[index]]
            else:
                ans += mapping[s[index]]

        ans += mapping[s[-1]]
        return ans


# @leet end
