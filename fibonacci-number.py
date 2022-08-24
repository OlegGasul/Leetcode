# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946

def fib(n: int) -> int:
    if n <= 2:
        return 1
    
    a = 1
    b = 1
    
    while n > 2:
        a, b = b, a + b
        n -= 1
    
    return b

print(fib(10))