def hammingDistance(x: int, y: int) -> int:
    if x == y:
        return 0
    
    result = 0
    while x > 0 or y > 0:
        result += (x & 1) ^ (y & 1)
        x = x >> 1 if x > 0 else 0
        y = y >> 1 if y > 0 else 0

    return result

print(hammingDistance(1, 4))
print(hammingDistance(3, 1))
print(hammingDistance(3, 0))
print(hammingDistance(0, 0))
print(hammingDistance(2 ** 31, 0))
print(hammingDistance(2 ** 31, 2 ** 10))
print(hammingDistance(2 ** 31, 23232232))