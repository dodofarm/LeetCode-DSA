# @leet start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        p1, p2 = 0, 0

        while p2 < len(nums):
            if nums[p2] != val:
                if p1 != p2:
                    nums[p1] = nums[p2]
                p1 += 1

            p2 += 1

        return p1


# @leet end
