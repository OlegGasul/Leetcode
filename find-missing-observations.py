def missingRolls(rolls, mean: int, n: int):
    total = mean * (len(rolls) + n) - sum(rolls)
    if total < 0:
        return []
    
    reminder = total % n
    value = total // n

    if value == 0 or value > 6 or (reminder > 0 and (6 - value) * n < reminder):
        return []
        
    result = [value] * n
    while reminder:
        for i in range(len(result)):
            result[i] += 1
            reminder -= 1
            
            if not reminder:
                break

    return result

print(missingRolls([4, 2, 2, 5, 4, 5, 4, 5, 3, 3, 6, 1, 2, 4, 2, 1, 6, 5, 4, 2, 3, 4, 2, 3, 3, 5, 4, 1, 4, 4, 5, 3, 6, 1, 5, 2, 3, 3, 6, 1, 6, 4, 1, 3], 2, 53))
print(missingRolls([6, 3, 4, 3, 5, 3], 1, 6))
print(missingRolls([3, 2, 4, 3], 4, 2))
print(missingRolls([1, 5, 6], 3, 4))
print(missingRolls([1, 2, 3, 4], 6, 4))