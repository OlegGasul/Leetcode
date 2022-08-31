def binaryGap(n: int) -> int:
    def isPowerOfTwo (x):
        return x and (not(x & (x - 1)))

    if isPowerOfTwo(n):
        return 0

    while n > 0 and n & 1 == 0:
        n >>= 1
        
    maxLength = 1
    current = 1

    while n > 0:
        if n & 1 == 1:
            maxLength = max(maxLength, current)
            current = 1
        else:
            current += 1
                
        n >>= 1
                
    return maxLength

print(binaryGap(22))
print(binaryGap(8))
print(binaryGap(6))
print(binaryGap(13))