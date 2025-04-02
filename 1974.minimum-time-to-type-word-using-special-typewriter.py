# @leet start
class Solution:
    def minTimeToType(self, word: str) -> int:
        seconds = 0
        pointer = 1
        for char in word:
            # + 1 to allow the distance to be cacl correctly since otherwise a would be 0
            char_value = ord(char) - ord("a") + 1
            # calculate the difference correctly, whether the pointer is before or after the char
            if pointer > char_value:
                difference = pointer - char_value
            else:
                difference = char_value - pointer
            # here we do the following: check whether the desired char is more than 13 characters away,
            # if it is it means that it's closer to go "the other way around" instead of walking said 13
            # chars or more. To calc the difference see this example:
            # pointer at 2, char at 24, the fastest way is to go 4 fields. The way to get there is 26 + 2 - 24 = 4
            if difference > 13 and pointer < char_value:
                difference = 26 + pointer - char_value
            elif difference > 13 and pointer > char_value:
                difference = 26 - pointer + char_value
            pointer = char_value
            seconds += difference + 1  # + 1 to type the actual letter

        return seconds


# perfect solution:
# interesting trick to do %26 to get the "optimal path"
# e.g. -4 % 26 = 22
# 26 - 22 = 4
# then the shortest path is picked using min
# additionally avoid +1 by using len(word) seems elegant
# class Solution:
#     def minTimeToType(self, word: str) -> int:
#         ans = len(word)
#         prev = "a"
#         for ch in word:
#             val = (ord(ch) - ord(prev)) % 26
#             ans += min(val, 26 - val)
#             prev = ch
#         return ans


# @leet end
