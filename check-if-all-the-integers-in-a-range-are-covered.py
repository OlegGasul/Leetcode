def isCovered(ranges, left: int, right: int) -> bool:
    count = right - left + 1
    values = [1] * count
        
    for r in ranges:
        for val in range(r[0], r[1] + 1):
            if val < left:
                continue
            if val > right:
                break
                
            if values[val - left] == 1:
                values[val - left] = 0
                count -= 1
                    
    return count == 0

print(isCovered([[1, 2], [3, 4], [5, 6]], 2, 5))
print(isCovered([[1, 10], [10, 20]], 21, 21))