def average(salary) -> float:
    total = 0
    minimum = float('inf')
    maximum = float('-inf')
        
    for value in salary:
        minimum = min(minimum, value)
        maximum = max(maximum, value)
        total += value
            
    return (total - (minimum + maximum)) / (len(salary) - 2)

print(average([4000, 3000, 1000, 2000]))
print(average([1000, 2000, 3000]))