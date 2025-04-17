from typing import List


# @leet start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix[0]) * len(matrix) - 1

        while start <= end:
            mid = (start + end) // 2
            row = mid // len(matrix[0])
            column = mid % len(matrix[0])
            val = matrix[row][column]
            if target == val:
                return True
            if target > val:
                start = mid + 1
            if target < val:
                end = mid - 1

        return False


# @leet end

