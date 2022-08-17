def findDuplicate(nums) -> int:
    n = len(nums) - 1
    requiredSum = int((n * (n + 1)) / 2)
    
    return sum(nums) - requiredSum
    
print(findDuplicate([1, 3, 4, 2, 2]))
print(findDuplicate([3, 1, 3, 4, 2]))