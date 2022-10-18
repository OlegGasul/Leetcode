def zeroFilledSubarray(nums) -> int:
    count = 0
    result = 0
        
    for num in nums:
        if num:
            if count:
                result += count * (count + 1) // 2
                    
            count = 0
        else:
            count += 1
                
    if count:
        result += count * (count + 1) // 2
            
    return result

print(zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]))
print(zeroFilledSubarray([0, 0, 0, 2, 0, 0]))