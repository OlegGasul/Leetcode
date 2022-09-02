def xorOperation(n: int, start: int) -> int:
    result = 0
    for i in range(n):
        result ^= start + 2 * i
        
    return result

print(xorOperation(5, 0))
print(xorOperation(4, 3))
print(xorOperation(10, 0))