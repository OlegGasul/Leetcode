def longestMountain(nums) -> int:
    length = len(nums)

    if length < 3:
        return 0

    longest = 0
    start = 0
    i = 1

    while i < length - 1:
        if nums[i] > nums[i - 1]:
            if nums[i] > nums[i + 1]:
                j = i + 1
                while j < length - 1 and nums[j + 1] < nums[j]:
                    j += 1
                
                longest = max(j - start + 1, longest)
                i = j
                start = j

        else:
            start = i

        i += 1

    return longest


print(longestMountain([2, 1, 4, 7, 3, 2, 8, 1]))
print(longestMountain([2, 1, 4, 7, 3, 1, 8, 0, 1]))
print(longestMountain([2, 1, 4, 7, 3, 2, 5]))
print(longestMountain([1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]))
