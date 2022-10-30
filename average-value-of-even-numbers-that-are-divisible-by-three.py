def averageValue(nums) -> int:
    values = []
        
    for num in nums:
        if num % 2 == 0 and num % 3 == 0:
            values.append(num)
                
    if not values:
        return 0
        
    return sum(values) // len(values)

print(averageValue([1, 3, 6, 10, 12, 15]))
print(averageValue([1, 2, 4, 7, 10]))