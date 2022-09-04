def minFlips(a: int, b: int, c: int) -> int:
    flips = 0
        
    while a or b or c:
        if c & 1 == 1 and (a & 1) | (b & 1) == 0:
            flips += 1
        elif c & 1 == 0:
            flips += (a & 1) + (b & 1)

        a >>= 1
        b >>= 1
        c >>= 1
                
    return flips

print(minFlips(2, 6, 5))
print(minFlips(4, 2, 7))
print(minFlips(1, 2, 3))