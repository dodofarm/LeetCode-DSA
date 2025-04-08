# pylint: skip-file
# nice simple solution to showcase python knowledge:
class Solution_one:
    def reverseWords(self, s: str) -> str:
        return " ".join(
            reversed(s.split())
        )  # Using split() removes ALL whitespace chars


# O(n) space complexity
class Solution_two:
    def reverseWords(self, s: str) -> str:
        str_arr = s.split(" ")
        ans = []
        for i in reversed(str_arr):
            if len(i) > 0:
                ans.append(i)

        return " ".join(ans)


# @leet start


class Solution:
    def reverseWords(self, s: str) -> str:
        # Reverse string and convert to list
        s = list(reversed(s))  # type: ignore
        print(s)

        def swap(left, right) -> None:
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        start, end = 0, 0
        while start < len(s):
            print("start", start)
            for index in range(start, len(s)):
                print(s[index])
                if s[index] == " ":
                    end += 1
                    start += 1
                else:
                    break
            print("start", start)

            for index in range(start, len(s)):
                if s[index] != " ":
                    end += +1
                else:
                    break
            print("pointer", end)

            swap(start, end)
            start = end + 1

        return s


# @leet end
