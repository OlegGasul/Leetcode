def decompressRLElist(nums):
    length = len(nums)
    if length % 2 != 0:
        return []
        
    result = []
        
    i = 0
    while i < length:
        result += [nums[i + 1]] * nums[i]
            
        i += 2
            
    return result

print(decompressRLElist([1, 2, 3, 4]))
print(decompressRLElist([1, 1, 2, 3]))