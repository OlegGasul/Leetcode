def sortArrayByParityII(nums):
    length = len(nums)
    evens = []
    odds = []
    
    for i in range(length):
        if nums[i] % 2 == 0:
            evens.append(nums[i])
        else:
            odds.append(nums[i])
                
    for i in range(length):
        nums[i] = evens.pop() if i % 2 == 0 else odds.pop()
        
    return nums

print(sortArrayByParityII([4, 2, 5, 7]))
print(sortArrayByParityII([2, 3]))