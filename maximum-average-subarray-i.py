def findMaxAverage(nums, k) -> float:
    length = len(nums)
    if length <= k:
        return sum(nums) / length

    current = 0
    
    for i in range(k):
        current += nums[i]
    
    maximum = current

    for j in range(i + 1, length):
        current -= nums[j - k]
        current += nums[j]
        maximum = max(maximum, current)

    return maximum / k


print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))