def productExceptSelf(nums):
    length = len(nums)
    
    prefix = [1] * (length + 1)
    postfix = [1] * (length + 1)
    result = [1] * length
    
    for i in range(length):
        j = length - i - 1
        
        left = nums[i]
        right = nums[j]
        
        prefix[i + 1] = prefix[i] * left
        postfix[j - 1] = postfix[j] * right
        
        if i >= j:
            result[i] = prefix[i] * postfix[i]
            result[j] = prefix[j] * postfix[j]
    
    return result

print(productExceptSelf([1, 2, 3, 4, 5]))