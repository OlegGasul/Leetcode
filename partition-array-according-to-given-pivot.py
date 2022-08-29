def pivotArray(nums, pivot: int):
    left = []
    right = []

    for num in nums:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            right.insert(0, num)

    return left + right

print(pivotArray([9, 12, 5, 10, 14, 3, 10], 10))