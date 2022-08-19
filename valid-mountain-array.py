def validMountainArray(arr) -> bool:
    length = len(arr)
    if length < 3:
        return False

    left = 0
    right = length - 1

    while left < length - 1:
        if arr[left] == arr[left + 1]:
            return False
        
        if arr[left] > arr[left + 1]:
            break

        left += 1

    if left == right or left == 0:
        return False

    while right > left:
        if arr[right] >= arr[right - 1]:
            return False

        right -= 1

    return left == right

print(validMountainArray([2, 1]))
print(validMountainArray([3, 5, 5]))
print(validMountainArray([0, 3, 2, 1]))
print(validMountainArray([1, 2, 3, 4, 3, 2, 1]))
print(validMountainArray([1, 2, 3, 4]))
print(validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))