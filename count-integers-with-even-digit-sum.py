def countEven(num: int) -> int:
    result = 0
    while num:
        if sum([int(x) for x in list(str(num))]) % 2 == 0:
            result += 1
        num -= 1
                
    return result

print(countEven(4))
print(countEven(30))
print(countEven(1000))