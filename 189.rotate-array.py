from collections import deque


# @leet start
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        arr: deque[int] = deque(nums)
        print(arr)
        for _ in range(k):
            tmp = arr.pop()
            arr.appendleft(tmp)

        print(list(arr))

        nums = list(arr)


# @leet end
