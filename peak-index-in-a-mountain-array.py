def peakIndexInMountainArray(arr):
    length = len(arr)
    if length < 3:
        return -1

    left = 0
    right = length - 1

    while left < right:
        middle = left + (right - left) // 2
        if arr[middle] > arr[middle - 1] and arr[middle] > arr[middle + 1]:
            return middle

        if arr[middle] > arr[middle - 1]:
            left = middle
        else:
            right = middle

    return -1
        

print(peakIndexInMountainArray([0, 1, 2, 3, 2, 1, 0]))
print(peakIndexInMountainArray([0, 10, 5, 2]))