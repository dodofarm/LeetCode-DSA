from typing import List


def quicksort(input_arr: List[int]) -> [int]:
    arr = input_arr.copy()

    def _quicksort(low, high) -> [int]:
        def partition(low, high) -> [int]:
            pivot = arr[high]
            pointer = low
            for i in range(low, high):
                if arr[i] < pivot:
                    if i != pointer:
                        arr[i], arr[pointer] = arr[pointer], arr[i]
                    pointer += 1

            arr[pointer], arr[high] = arr[high], arr[pointer]
            return pointer

        if low < high:
            pivot = partition(low, high)
            _quicksort(low, pivot - 1)
            _quicksort(pivot + 1, high)

    _quicksort(0, len(arr) - 1)
    return arr


test_array = [2, 1, 7, 4, 9, 3, 7, 3, 5, 1, 6]
print(quicksort(test_array))
