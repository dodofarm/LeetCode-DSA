# @leet start
class Solution:
    def intToRoman(self, num: int) -> str:
        mapping: dict[int, str] = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        ans = ""

        for denomination, roman_number in mapping.items():
            multiple = num // denomination
            num -= multiple * denomination
            for _ in range(multiple):
                ans += roman_number

        return ans


# @leet end
