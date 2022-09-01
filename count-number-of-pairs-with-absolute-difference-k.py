from collections import Counter

def countKDifference(nums, k: int) -> int:
    counter = Counter()
    result = 0
        
    for i in range(len(nums)):
        val1 = nums[i] - k
        val2 = nums[i] + k
            
        if val1 in counter:
            result += counter[val1]
        
        if val2 in counter:
            result += counter[val2]
        
        counter[nums[i]] += 1
                
    return result

print(countKDifference([1, 2, 2, 1], 1))
print(countKDifference([1, 3], 3))