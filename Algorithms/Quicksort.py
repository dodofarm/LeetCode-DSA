def quicksort(input: [int]) -> [int]:
    arr = input.copy()
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    pointer = 0
    for i in range(len(arr) - 1):
        if arr[i] < pivot:
            # if pointer != i:
            arr[i], arr[pointer] = arr[pointer], arr[i]
            pointer += 1

    arr[-1], arr[pointer] = arr[pointer], arr[-1]  # swap pointer with pivot
    # sort again parts before and after pivot
    return quicksort(arr[:pointer]) + [arr[pointer]] + quicksort(arr[pointer + 1 :])


test_array = [2, 1, 7, 4, 9, 3, 7, 3, 5, 1, 6]
print(quicksort(test_array))
