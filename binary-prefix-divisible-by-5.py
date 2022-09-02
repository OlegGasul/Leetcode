def prefixesDivBy5(nums):
    length = len(nums)
        
    result = []
        
    num = int(''.join([str(x) for x in nums]), 2)
        
    i = 0
    while i < length:
        result.insert(0, num % 5 == 0)
        num >>= 1
        i += 1
            
    return result

print(prefixesDivBy5([0, 1, 1]))
print(prefixesDivBy5([1, 1, 1]))