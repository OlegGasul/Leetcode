def findKDistantIndices(nums, key: int, k: int):
    indexes = set()
    length = len(nums)
        
    for i in range(length):
        if nums[i] == key:
            for j in range(max(i - k, 0), min(i + k + 1, length)):
                indexes.add(j)
                    
    result = list(indexes)
    result.sort()
        
    return result

print(findKDistantIndices([3, 4, 9, 1, 3, 9, 5], 9, 1))
print(findKDistantIndices([2, 2, 2, 2, 2], 2, 2))