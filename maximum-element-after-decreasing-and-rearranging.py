def maximumElementAfterDecrementingAndRearranging(arr) -> int:
    arr.sort()
    arr[0] = 1

    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > 1:
            arr[i] = arr[i - 1] + 1

    return arr[-1]

print(maximumElementAfterDecrementingAndRearranging([1, 1, 2, 2, 4, 4, 10, 10]))
print(maximumElementAfterDecrementingAndRearranging([1, 10, 10, 10, 10, 10, 10, 10]))
print(maximumElementAfterDecrementingAndRearranging([1, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
print(maximumElementAfterDecrementingAndRearranging([1, 1, 1, 1, 1]))
print(maximumElementAfterDecrementingAndRearranging([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 10]))