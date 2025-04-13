from typing import List


# @leet start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        anagram_frequency: List[int] = [0] * 26
        subarray_frequency: List[int] = [0] * 26
        matches = 0
        ans: List[int] = []

        for char in range(len(p)):
            ascii_val_p = ord(p[char]) - ord("a")
            ascii_val_s = ord(s[char]) - ord("a")
            anagram_frequency[ascii_val_p] += 1
            subarray_frequency[ascii_val_s] += 1

        for i in range(26):
            if anagram_frequency[i] == subarray_frequency[i]:
                matches += 1

        if matches == 26:
            ans.append(0)

        print(anagram_frequency)
        print(subarray_frequency)
        for i in range(len(p), len(s)):
            first_char = ord(s[i - len(p)]) - ord("a")
            second_char = ord(s[i]) - ord("a")
            subarray_frequency[first_char] -= 1
            if subarray_frequency[first_char] + 1 == anagram_frequency[first_char]:
                matches -= 1
            elif subarray_frequency[first_char] == anagram_frequency[first_char]:
                matches += 1
            subarray_frequency[second_char] += 1
            if subarray_frequency[second_char] - 1 == anagram_frequency[second_char]:
                matches -= 1
            elif subarray_frequency[second_char] == anagram_frequency[second_char]:
                matches += 1
            if matches == 26:
                ans.append(i - len(p) + 1)

        return ans


# @leet end

