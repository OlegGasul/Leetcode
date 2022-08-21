def integerReplacement(n: int) -> int:
    if n == 1:
        return 0
    
    count = 0
    
    while n > 1:
        if n & (n - 1) == 0:
            while n > 1:
                n >>= 1
                count += 1
            return count
        
        if n % 2 == 0:
            n //= 2
        else:
            if (n - 1) & ((n - 1) - 1) == 0:
                n -= 1
            elif (n + 1) & n == 0:
                n += 1
            elif ((n - 1) // 2) % 2 == 0 or n == 2:
                n -= 1
            else:
                n += 1
        
        count += 1

    return count


# print(integerReplacement(8))
# print(integerReplacement(3))
print(integerReplacement(10000))
