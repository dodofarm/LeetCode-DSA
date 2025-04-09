from typing import List


def quicksort(input_arr: List[int]) -> List[int]:
    """
    Quicksort algorithm that sorts an array of numbers in O(nlogn) time
    """
    arr = input_arr.copy()

    def _quicksort(start: int, end: int) -> None:
        if end - start <= 1:
            return
        pivot = arr[end]

        pointer = start
        for i in range(start, end):
            if arr[i] < pivot:
                if i != pointer:
                    arr[i], arr[pointer] = arr[pointer], arr[i]
                pointer += 1

        arr[pointer], arr[end] = arr[end], arr[pointer]
        _quicksort(start, pointer - 1)
        _quicksort(pointer + 1, end)

    _quicksort(0, len(arr) - 1)
    return arr


test_array = [2, 1, 7, 4, 9, 3, 7, 3, 5, 1, 6]

print(quicksort(test_array))
