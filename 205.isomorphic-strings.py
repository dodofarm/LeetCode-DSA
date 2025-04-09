from collections import defaultdict
from typing import List


# @leet start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def fill_dict_with_frequency(dictionary: dict[str, int], string: str) -> None:
            for i in string:
                dictionary[i] += 1

        frequency_one: dict[str, int] = defaultdict(int)
        frequency_two: dict[str, int] = defaultdict(int)
        fill_dict_with_frequency(frequency_one, s)
        fill_dict_with_frequency(frequency_two, t)
        # mapping: dict[str, str] = {}

        # print(frequency_one, frequency_two)
        # bucket: List[List[str]] = [[]] * 26
        bucket: List[List[str]] = [[] for i in range(0, len(s) + 1)]
        for char, frequency in frequency_one.items():
            # print(char, frequency)
            # print(bucket)
            bucket[frequency].append(char)
            # print(bucket)

        for letter_two, frequency in frequency_two.items():
            # print(frequency)
            # print(bucket)
            if bucket[frequency]:
                letter_one = bucket[frequency].pop(0)
                # mapping[letter_one] = letter_two
            else:
                return False

        # temp = list(s)
        # for i in range(len(s)):
        #     temp[i] = mapping[s[i]]
        # print(mapping)
        # print(temp)
        # if not "".join(temp) == t:
        #     return False
        return True


# @leet end

