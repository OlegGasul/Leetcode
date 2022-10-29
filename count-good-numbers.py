# Time limit exceed for huge values
def countGoodNumbers(n: int) -> int:
    primes = n // 2
    evens = n - primes
        
    evens = 5 ** evens if evens > 0 else 1
    primes = 4 ** primes if primes > 0 else 1
        
    result = evens * primes
        
    return result % (10 ** 9 + 7)

# Passed
def countGoodNumbers2(n: int) -> int:
    reminder = n % 2
    n -= reminder
    
    result = pow(20, n // 2, 10 ** 9 + 7)
    if reminder == 1:
        result *= 5
    
    return result % (10**9 + 7)

print(countGoodNumbers(50))
print(countGoodNumbers2(806166225460393))