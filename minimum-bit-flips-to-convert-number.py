def minBitFlips(start: int, goal: int) -> int:
    flips = 0
        
    while start or goal:
        if (start & 1) != (goal & 1):
            flips += 1
        start >>= 1
        goal >>= 1
                
    return flips

print(minBitFlips(10, 7))
print(minBitFlips(3, 4))