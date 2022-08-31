def sortEvenOdd(nums):
    length = len(nums)
    evens = []
    odds = []
    
    for i in range(length):
        if i % 2 == 0:
            evens.append(nums[i])
        else:
            odds.append(nums[i])
                
    evens.sort(reverse = True)
    odds.sort()
        
    for i in range(length):
        nums[i] = evens.pop() if i % 2 == 0 else odds.pop()
            
    return nums

print(sortEvenOdd([4, 1, 2, 3]))
print(sortEvenOdd([2, 1]))