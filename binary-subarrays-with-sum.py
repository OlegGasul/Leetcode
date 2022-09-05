import collections

def numSubarraysWithSum(nums, goal: int) -> int:
    dp = [0]
    for x in nums:
        dp.append(dp[-1] + x)
        
    count = collections.Counter()
    
    result = 0
    for x in dp:
        result += count[x]
        count[x + goal] += 1

    return result

print(numSubarraysWithSum([1, 0, 1, 0, 1], 2))