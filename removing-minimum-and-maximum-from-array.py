def minimumDeletions(nums) -> int:
    length = len(nums)
    if length <= 2:
        return length

    minimum = float('inf')
    maximium = float('-inf')
    minimumIndex = -1
    maximiumIndex = -1

    for i in range(length):
        if nums[i] < minimum:
            minimum = nums[i]
            minimumIndex = i
        if nums[i] > maximium:
            maximium = nums[i]
            maximiumIndex = i

    left, right = min(minimumIndex, maximiumIndex), max(minimumIndex, maximiumIndex)
    
    return min(right + 1, length - left, (left + 1) + (length - right))


print(minimumDeletions([2, 10, 7, 5, 4, 1, 8, 6]))
print(minimumDeletions([1, 10, 7, 5, 4, 2, 8, 6]))
print(minimumDeletions([6, 8, 7, 5, 4, 2, 10, 1]))
print(minimumDeletions([6, 8, 7, 10, 1, 5, 4, 2]))