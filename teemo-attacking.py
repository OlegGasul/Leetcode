def findPoisonedDuration(timeSeries, duration: int) -> int:
    result = 0
        
    for i in range(1, len(timeSeries)):
        if timeSeries[i] - timeSeries[i - 1] >= duration:
            result += duration
        else:
            result += timeSeries[i] - timeSeries[i - 1]
                
        result += duration
        
    return result

print(findPoisonedDuration([1, 4], 2))
print(findPoisonedDuration([1, 2], 2))
print(findPoisonedDuration([1, 2, 3, 4, 5], 10))