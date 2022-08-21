def containsNearbyDuplicate(nums, k: int) -> bool:
    length = k + 1
    if length >= len(nums):
        return len(nums) != len(set(nums))
    
    digits = set()

    for i in range(length):
        digits.add(nums[i])

    if len(digits) < length:
        return True

    for j in range(i + 1, len(nums)):
        digits.remove(nums[j - length])
        digits.add(nums[j])

        if len(digits) < length:
            return True

    return False


# print(containsNearbyDuplicate([1, 2, 3, 1], 3))
# print(containsNearbyDuplicate([1, 0, 1, 1], 1))
# print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
print(containsNearbyDuplicate([1, 2, 1], 1))
