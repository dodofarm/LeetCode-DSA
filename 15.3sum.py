from typing import List


# @leet start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pointer = len(nums) - 1
        ans: List[List[int]] = []
        while 0 < pointer - 1:
            for i in range(start, pointer):
                target = nums[start] - nums[pointer]
                if nums[i] == target:
                    ans.append([start, i, pointer])

        return ans


# @leet end
