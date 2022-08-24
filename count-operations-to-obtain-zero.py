def countOperations(num1: int, num2: int) -> int:
    count = 0
    
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            count += num1 // num2
            num1 = num1 % num2
        else:
            count += num2 // num1
            num2 = num2 % num1

    return count


print(countOperations(2, 3))
print(countOperations(10, 10))
print(countOperations(10, 12))
print(countOperations(0, 0))