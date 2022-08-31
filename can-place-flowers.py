def canPlaceFlowers(flowerbed, n: int) -> bool:
    length = len(flowerbed)
    flowerbed.append(0)
        
    i = 0
    while n > 0 and i < length:
        if flowerbed[i] == flowerbed[i - 1] == flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            n -= 1
        i += 1
            
    return n == 0

print(canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(canPlaceFlowers([1, 0, 0, 0, 1], 2))