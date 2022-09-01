from collections import Counter

def subarraysDivByK(nums, k: int) -> int:
    prefixSum = Counter()
    prefixSum[0] = 1
    
    curSum = 0
    result = 0
    
    for num in nums:
        curSum += num 
        result += prefixSum[curSum % k]
        prefixSum[curSum % k] += 1

    return result

print(subarraysDivByK([4, 5, 0, -2, -3, 1], 5))