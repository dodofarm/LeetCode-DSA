from typing import List


def binary_search(arr: List[int], val: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > val:
            right = mid - 1
        elif arr[mid] < val:
            left = mid + 1
        else:
            return mid

    return -1


my_arr = [1, 52, 57, 78, 79, 85, 89, 90, 96, 99]
print(binary_search(my_arr, 89))
