def checkIfExist(nums) -> bool:
    visited = set()
        
    for i in range(len(nums)):
        if 2 * nums[i] in visited or (nums[i] % 2 == 0 and (nums[i] // 2) in visited):
            return True
            
        visited.add(nums[i])
            
    return False

print(checkIfExist([10, 2, 5, 3]))
print(checkIfExist([7, 1, 14, 11]))
print(checkIfExist([3, 1, 7, 11]))