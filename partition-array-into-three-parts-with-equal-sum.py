def canThreePartsEqualSum(nums) -> bool:
    length = len(nums)
    if length < 3:
        return False
    
    total = sum(nums)
    if total % 3 != 0:
        return False

    partSum = total // 3
    
    left = 0
    right = length - 1

    leftSum = nums[left]
    rightSum = nums[right]

    while left < right:
        if leftSum != partSum:
            left += 1
            leftSum += nums[left]

        if rightSum != partSum:
            right -= 1
            rightSum += nums[right]

        if leftSum == rightSum and leftSum == partSum:
            break

    return right - left > 1
    

print(canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))
print(canThreePartsEqualSum([6, 1, 1, 13, -1, 0, -10, 20]))
print(canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
print(canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))
print(canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))