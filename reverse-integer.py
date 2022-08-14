def reverse(x: int) -> int:
    if x == 0:
        return 0
    
    is_negative = x < 0
    x = abs(x)
    
    if x < 10:
        return x * -1 if is_negative else x
    
    result = 0
    
    while x > 0:
        result = result * 10 + (x % 10)
        x = x // 10
        if result >= 2 ** 31 - 1:
            return 0
    
    return result * -1 if is_negative else result

print('-123 = ' + str(reverse(-123)))
print('123 = ' + str(reverse(-123)))
print('1534236469 = ' + str(reverse(1534236469)))
