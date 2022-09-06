def sumBase(n: int, k: int) -> int:
    if k > 10:
        return "Wrong arguments"
    
    result = []

    while n >= k:
        result.append(n % k)
        n //= k

    result.append(n)
    
    return sum(result)

print(sumBase(42, 2))
print(sumBase(34, 6))
print(sumBase(10, 10))
print(sumBase(10, 2))
print(sumBase(6, 6))