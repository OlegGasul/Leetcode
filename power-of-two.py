def isPowerOfTwo(n: int) -> bool:
    return (n & (n - 1) == 0) and n != 0

print(isPowerOfTwo(16))
print(isPowerOfTwo(12))