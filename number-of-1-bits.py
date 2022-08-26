def hammingWeight(n: int) -> int:
    return sum([int(x) for x in bin(n)[2:]])
    

print(hammingWeight(11))