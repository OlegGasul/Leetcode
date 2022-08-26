def findMaxLength(nums) -> int:
    length = len(nums)

    arr = [-2] * (2 * length + 1)
    arr[length] = -1
    
    maxLen = 0
    count = 0

    for i in range(length):
        count += 1 if nums[i] == 1 else -1
        if arr[count + length] >= -1:
            maxLen = max(maxLen, i - arr[count + length])
        else:
            arr[count + length] = i

        print(arr)

    return maxLen


# print(findMaxLength([0, 1, 1, 1, 1, 1, 1]))
# print(findMaxLength([1, 1, 1, 1, 1, 1, 1, 1]))
# print(findMaxLength([0, 1, 0]))
# print(findMaxLength([0, 1, 0, 1]))
print(findMaxLength([0, 1, 0, 1, 0, 0, 0, 0, 0, 0]))
# print(findMaxLength([0]))
# print(findMaxLength([]))
# print(findMaxLength([0, 0, 0, 0, 1, 1, 1, 0, 0, 0]))
# print(findMaxLength([1, 1, 0, 0, 0, 0, 0, 0, 1, 1]))

# print(findMaxLength([0, 1, 1, 0, 1, 1, 1, 0]))
# print(findMaxLength([0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1]))
