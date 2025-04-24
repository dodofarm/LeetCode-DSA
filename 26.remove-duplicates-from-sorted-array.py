# in-place O(n) time, O(1) space
# @leet start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        p1, p2 = 1, 1
        while p2 < len(nums):
            if nums[p2] != nums[p2 - 1]:
                # k += 1
                if p1 != p2:
                    nums[p1] = nums[p2]
                p1 += 1
            p2 += 1

        return p1


# @leet end
# 112
