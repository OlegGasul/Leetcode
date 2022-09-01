def tribonacci(n: int) -> int:
    numbers = [0] * 38
    numbers[1] = 1
    numbers[2] = 1
        
    if n <= 2:
        return numbers[n]
        
    for i in range(2, n + 1):
        numbers[i] = numbers[i - 1] + numbers[i - 2] + numbers[i - 3]
            
    return numbers[n]

print(tribonacci(4))
print(tribonacci(25))