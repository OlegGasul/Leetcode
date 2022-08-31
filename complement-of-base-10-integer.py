import math

def bitwiseComplement(n: int) -> int:
    if n == 0:
        return 1
        
    mask = int('1' * (math.floor(math.log2(n)) + 1), 2)
    return n ^ mask

print(bitwiseComplement(5))
print(bitwiseComplement(10))