def twoSum(numbers, target: int):
    left = 0
    right = len(numbers) - 1

    while left < right:
        value = numbers[left] + numbers[right]
        if value == target:
            return [left + 1, right + 1]
        
        if value < target:
            left += 1
        else:
            right -= 1

    return []

    

print(twoSum([2, 7, 11, 15], 9))
print(twoSum([-1, 0], -1))
print(twoSum([2, 3, 4], 6))
print(twoSum([2, 3, 4], 0))