def subtractProductAndSum(self, n: int) -> int:
    product = 1
    total = 0
        
    while n:
        value = n % 10
        product *= value
        total += value
        n //= 10
            
    return product - total