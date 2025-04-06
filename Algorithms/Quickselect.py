def quickselect(input_arr: [int], k) -> int:
    arr = input_arr.copy()

    def partition(start, end, k) -> int:
        pivot = end
        pointer = start
        for i in range(start, end):
            if arr[i] < arr[pivot]:
                if i != pointer:
                    arr[i], arr[pointer] = arr[pointer], arr[i]
                pointer += 1

        arr[pointer], arr[pivot] = arr[pivot], arr[pointer]

        if pointer > k:  # pylint: disable=no-else-return
            return partition(start, pointer - 1, k)
        elif pointer < k:
            return partition(pointer + 1, end, k)
        else:
            return arr[pointer]

    k = len(arr) - k
    return partition(0, len(arr) - 1, k)


test_array = [2, 1, 7, 4, 9, 3, 7, 3, 5, 1, 6]
print(quickselect(test_array, 4))
