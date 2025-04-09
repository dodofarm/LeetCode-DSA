from typing import List


# @leet start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        count: dict[int, List[int]] = {}
        for i in range(len(nums)):
            if i > k:
                pass
            if count.get(nums[i]):
                for j in count[nums[i]]:
                    if abs(i - j) <= k:
                        return True

            count[nums[i]] = []
            count[nums[i]].append(i)
        return False


# @leet end

