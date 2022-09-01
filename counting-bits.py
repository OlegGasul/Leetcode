def countBits(n: int):
    result = [0] * (n + 1)
    
    def countBits(num):
        count = 0
        klop = num
        
        while num:
            num = num & (num - 1)
            count += 1
            
        return count
        
    for i in range(n + 1):
        result[i] = countBits(i)
            
    return result

print(countBits(5))
print(countBits(100))