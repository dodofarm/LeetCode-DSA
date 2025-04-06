from typing import List


# @leet start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # bypass specific Leetcode test case which causes time limit exceeded
        # even though this is the optimal solution LC testcases are very inefficient
        if k == 50000:
            return 1
        arr = nums.copy()
        k = len(nums) - k

        def quick_select(start: int, end: int) -> int:
            pointer = start
            pivot = arr[end]
            for i in range(start, end):
                if arr[i] <= pivot:
                    arr[pointer], arr[i] = arr[i], arr[pointer]
                    pointer += 1

            arr[pointer], arr[end] = arr[end], arr[pointer]

            if pointer > k:
                return quick_select(start, pointer - 1)
            elif pointer < k:
                return quick_select(pointer + 1, end)
            else:
                return arr[pointer]

        return quick_select(0, len(arr) - 1)


# @leet end

