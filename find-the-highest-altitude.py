def largestAltitude(gain) -> int:
    result = 0
    altitude = 0
        
    for i in range(len(gain)):
        altitude += gain[i]
        result = max(result, altitude)
            
    return result

print(largestAltitude([-5, 1, 5, 0, -7]))
print(largestAltitude([-4, -3, -2, -1, 4, 3, 2]))