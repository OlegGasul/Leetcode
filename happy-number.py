def isHappy(n: int) -> bool:
    if n == 1:
        return True

    seen = set()
    
    while True:
        sum = 0
        while n != 0:
            n, digit = divmod(n, 10)
            sum += digit ** 2
        
        if sum == 1:
            return True

        n = sum
        if n in seen:
            return False
        
        seen.add(n)

    return False

print(isHappy(19))
print(isHappy(2))
print(isHappy(1))
print(isHappy(7))