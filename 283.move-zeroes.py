from typing import List


# Not as good because popping and appending is more expensive than swapping the elements
class Solution_one:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums) - 1
        for i in range(length, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)


# @leet start


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        i = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


# @leet end

