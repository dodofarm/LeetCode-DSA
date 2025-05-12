class Solution_one:
    def maximumTripletValue(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                res = nums[i] - nums[j]
                for k in range(j + 1, len(nums)):
                    ans = max(ans, res * nums[k])

        return ans


# @leet start


class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    ans = max(ans, (nums[i] - nums[j]) * nums[k])

        return ans


# @leet end
