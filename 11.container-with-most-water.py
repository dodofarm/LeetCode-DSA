class Solution_one:
    def maxArea(self, height: list[int]) -> int:
        p1, p2 = 0, len(height) - 1
        # max_area = min(height[p1], height[p2]) * (p2 - p1)
        max_area = 0

        while p1 < p2:
            max_area = max(max_area, min(height[p1], height[p2]) * (p2 - p1))
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return max_area


# @leet start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        p1, p2 = 0, len(height) - 1
        ans = 0

        while p1 < p2:
            ans = max(ans, min(height[p1], height[p2]) * (p2 - p1))
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1

        return ans


# @leet end
