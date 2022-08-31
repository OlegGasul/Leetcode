def countPrimeSetBits(left: int, right: int) -> int:
    primes = set([2, 3, 5, 7, 11, 13, 17, 19])
        
    def calculateSetBits(num):
        result = 0
        while num > 0:
            result += num & 1
            num >>= 1
        return result
        
    num = left
    result = 0
        
    while num <= right:
        if calculateSetBits(num) in primes:
            result += 1
        num += 1
    
    return result

print(countPrimeSetBits(6, 10))
print(countPrimeSetBits(10, 15))
print(countPrimeSetBits(10, 15000))