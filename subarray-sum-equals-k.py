def subarraySum(nums, k: int) -> int:
    left = 0
    right = 0

    length = len(nums)
    
    dp = [0] * length
    dp[0] = nums[0]
    
    for i in range(1, length):
        dp[i] = dp[i - 1] + nums[i]

    # print(dp)

    count = 0

    while left < length and right < length:
        sum = dp[right] - dp[left] + nums[left]

        # print('left = ' + str(left))
        # print('right = ' + str(right))
        # print('sum = ' + str(sum))
        # print()

        if sum == k:
            count += 1
            
            if left == right:
                right += 1
            left += 1
        elif sum < k:
            if right == length - 1:
                left += 1
            else:
                right += 1
        elif sum > k:
            if left == right:
                right += 1
            left += 1

    return count
        

# [1, 2, 4, 0, 7, 2, 5]
print(subarraySum([1, 1, 1], 2))
print(subarraySum([1, 2, 3], 3))
print(subarraySum([1, 2, 4, 0, 7, 2, 5], 7))

# Not working for zeros
# print(subarraySum([-1, -1, 1, 1, -1], 0))
# print(subarraySum([1, -1, 0], 0))