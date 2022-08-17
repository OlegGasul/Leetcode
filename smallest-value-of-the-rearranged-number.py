import functools

def smallestNumber(num: int) -> int:
    if abs(num) < 10:
        return num
    
    isNegative = num < 0

    digits = [d for d in str(abs(num))]

    def compare(n, m):
        if isNegative:
            if m > n:
                return 1
            else:
                return -1
        else:
            if n > m:
                return 1
            else:
                return -1
            

    digits = sorted(digits, key = functools.cmp_to_key(compare))

    if isNegative:
        return '-' + ''.join(digits)
    else:
        if digits[0] == '0':
            for i in range(1, len(digits)):
                if digits[i] != '0':
                    digits[0], digits[i] = digits[i], digits[0]
                    break

        return ''.join(digits)

print(smallestNumber(310))
print(smallestNumber(-7605))
print(smallestNumber(3))
print(smallestNumber(0))