# @leet start
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums


# @leet end
