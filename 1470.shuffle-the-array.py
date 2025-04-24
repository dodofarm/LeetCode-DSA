# @leet start
class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        ans: list[int] = []

        for i in range(len(nums) // 2):
            ans.append(nums[i])
            ans.append(nums[i + n])

        return ans


# @leet end
