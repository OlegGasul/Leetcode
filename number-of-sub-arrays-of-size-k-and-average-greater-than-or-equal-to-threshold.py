def numOfSubarrays(nums, k: int, threshold: int) -> int:
    length = len(nums)

    if length == k:
        if sum(nums) // length >= threshold:
            return 1

    result = 0
    total = 0
    for i in range(k):
        total += nums[i]

    if total // k >= threshold:
        result += 1

    for i in range(k, length):
        total -= nums[i - k]
        total += nums[i]
        if total // k >= threshold:
            result += 1

    return result

    
print(numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))