def getStartDigit(value):
    if value < 10:
        return value
    
    s = str(value)
    first = int(s[0])
    second = int(s[1])

    incr = 1 if second > first + 1 else 0
    return first + incr



def sequentialDigits(low: int, high: int):
    if low > high:
        return []

    lowStr = str(low)
    left = len(lowStr)
    right = len(str(high))

    if left > right:
        return []
    
    result = []
    
    start = low
    firstDigit = getStartDigit(start)

    length = left
    while length <= right:
        while firstDigit + length - 1 <= 9:
            nums = list(range(firstDigit, firstDigit + length))
            value = int(''.join(str(x) for x in nums))
            
            if value > high:
                break

            result.append(value)
            firstDigit += 1

        length += 1
        start = int(''.join(str(i) for i in range(1, length)))
        firstDigit = 1

    return result


print(sequentialDigits(100, 800))
print(sequentialDigits(124, 800))
print(sequentialDigits(58, 155))

print(sequentialDigits(30099, 51208))
