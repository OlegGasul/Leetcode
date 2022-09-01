def countPairs(nums, k: int) -> int:
    indexes = {}
        
    result = 0
    for i in range(len(nums)):
        if nums[i] in indexes:
            j = 0
            ids = indexes[nums[i]]
            while j < len(ids):
                if (ids[j] * i) % k == 0:
                    result += 1
                j += 1
                
            ids.append(i)
        else:
            indexes[nums[i]] = [i]
        
    return result

print(countPairs([3, 1, 2, 2, 2, 1, 3], 2))
print(countPairs([1, 2, 3, 4], 1))