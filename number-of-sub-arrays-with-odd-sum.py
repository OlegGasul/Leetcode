def numOfSubarrays(nums) -> int:
    temp = [1, 0]
    result = 0
    val = 0

    for i in range(len(nums)):
        val = ((val + nums[i]) % 2 + 2) % 2
        temp[val] += 1
    
    result = (temp[0] * temp[1])
    return result % 1000000007 

print(numOfSubarrays([1, 3, 5]))
print(numOfSubarrays([2, 4, 6]))
print(numOfSubarrays([2, 4, 6, 1, 7, 2, 1, 3]))
print(numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))