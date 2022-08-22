def isPossibleDivide(nums, k: int) -> bool:
    nums = sorted(nums)

    if len(nums) % k == 1:
        return False
    
    while nums:
        count = k
        
        if len(nums) < k:
            return False
        
        i = 0
        current = nums[0] - 1

        while i < len(nums):
            if nums[i] - current == 1:
                current = nums[i]
                nums.pop(i)
                count -= 1
            else:
                i += 1

            if count == 0:
                break

        if count > 0:
            return False

    return True


    

# print(isPossibleDivide([1, 2, 3, 3, 4, 4, 5, 6], 2))
# print(isPossibleDivide([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3))
# print(isPossibleDivide([1, 2, 3, 4], 3))
# print(isPossibleDivide([1, 2, 3, 3, 4, 4, 5, 6], 4))
print(isPossibleDivide([2, 5, 6, 8, 9, 10], 3))
