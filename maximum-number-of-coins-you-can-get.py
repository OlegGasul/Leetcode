def maxCoins(piles) -> int:
    piles = sorted(piles)
        
    result = 0
    while piles:
        piles.pop()
        result += piles.pop()
        piles.pop(0)        
    return result

print(maxCoins([2, 4, 1, 2, 7, 8]))
print(maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]))