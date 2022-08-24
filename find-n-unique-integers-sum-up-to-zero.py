def sumZero(n: int):
    if n == 1:
        return [0]
    
    result = []
    
    num = 1
    
    while num <= n // 2:
        result.append(num)
        result.append(-num)
        num += 1

    if n % 2 == 1:
        result.append(0)

    return result



print(sumZero(5))