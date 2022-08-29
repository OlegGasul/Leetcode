def hammingWeight(n: int) -> int:
    result = 0

    while n > 0:
        result += n & 1
        n >>= 1

    return result
    

print(hammingWeight(11))