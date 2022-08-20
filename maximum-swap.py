def maximumSwap(num: int) -> int:
    nums = list(str(num))
    length = len(nums)
    
    maxIndex = length - 1
    dp = [0] * length
    
    for i in reversed(range(length)):
        if nums[i] > nums[maxIndex]:
            maxIndex = i
            dp[i] = i
        else:
            dp[i] = maxIndex

    # print(dp)

    for i in range(length):
        if i == dp[i]:
            continue
        
        if nums[i] < nums[dp[i]]:
            nums[i], nums[dp[i]] = nums[dp[i]], nums[i]
            break

    return ''.join(nums)
    

print(maximumSwap(27361))
print(maximumSwap(54321))
print(maximumSwap(12345))
print(maximumSwap(98368))
print(maximumSwap(2736))